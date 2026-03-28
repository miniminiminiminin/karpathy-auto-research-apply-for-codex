import asyncio
from pathlib import Path

from codex_writer.jobs.model import BatchResult, JobItem, JobSpec
from codex_writer.output.write import write_result
from codex_writer.pipeline.load import load_pipeline_payload
from codex_writer.pipeline.run import run_pipeline_for_item
from codex_writer.queue.store import (
    cleanup_job_dir,
    create_job,
    iso_now,
    load_items,
    record_completed_job,
    save_job_state,
    summarize_items,
    update_item_state,
)
from codex_writer.state.journal import append_jsonl
from codex_writer.stop.token import StopToken
from codex_writer.sdk.result import GenerationOutput
from codex_writer.template.render import render_prompt

MAX_ATTEMPTS = 3


def choose_concurrency(item_count: int, requested: int | None) -> int:
    if item_count <= 0:
        return 1
    if requested is not None:
        return max(1, min(requested, item_count))
    return min(item_count, 4)


async def run_batch(
    spec: JobSpec,
    items: list[JobItem],
    client: object,
    stop_token: StopToken | None = None,
    job_dir: Path | None = None,
) -> BatchResult:
    active_job_dir = job_dir or create_job(spec, items)
    all_items = load_items(active_job_dir)
    counts = summarize_items(active_job_dir, all_items)
    state = {
        "status": "running",
        "item_count": len(all_items),
        "succeeded": counts["succeeded"],
        "failed": counts["failed"],
        "cancelled": counts["cancelled"],
        "stop_requested": bool(stop_token and stop_token.requested),
        "started_at": iso_now(),
    }
    save_job_state(active_job_dir, state)
    semaphore = asyncio.Semaphore(choose_concurrency(len(items), spec.concurrency))
    tasks = [
        _run_item(
            active_job_dir,
            spec,
            item,
            client,
            semaphore,
            stop_token,
        )
        for item in items
    ]
    results = await asyncio.gather(*tasks)
    counts = summarize_items(active_job_dir, all_items)
    state["succeeded"] = counts["succeeded"]
    state["failed"] = counts["failed"]
    state["cancelled"] = counts["cancelled"]
    state["stop_requested"] = bool(stop_token and stop_token.requested)
    state["status"] = "stopped" if "cancelled" in results else "completed"
    state["tokens_used"] = sum(_token_count(result) for result in results)
    if state["status"] == "completed":
        state["completed_at"] = iso_now()
    save_job_state(active_job_dir, state)
    _cleanup_success(active_job_dir, spec, state)
    return BatchResult(
        spec.job_id,
        len(all_items),
        counts["succeeded"],
        counts["failed"],
        counts["cancelled"],
        int(state["tokens_used"]),
    )


async def _run_item(
    job_dir: Path,
    spec: JobSpec,
    item: JobItem,
    client: object,
    semaphore: asyncio.Semaphore,
    stop_token: StopToken | None,
) -> str | GenerationOutput:
    async with semaphore:
        update_item_state(job_dir, item, {"status": "running"})
        append_jsonl(job_dir / "events.jsonl", {"event": "running", "filename": item.filename})
        prompt = render_prompt(spec.prompt_template, item.variables) if spec.prompt_template else ""
        pipeline = load_pipeline_payload(spec.pipeline) if spec.pipeline else None
        feedback = ""
        for attempt in range(1, MAX_ATTEMPTS + 1):
            if stop_token and stop_token.requested:
                _cancel_item(job_dir, item, attempt - 1)
                return "cancelled"
            try:
                if pipeline is not None:
                    result = await run_pipeline_for_item(pipeline, item, spec.output_dir, client)
                    tokens_used = result.tokens_used
                    path = result.final_path
                    payload: dict[str, object] = {
                        "status": "succeeded",
                        "attempts": attempt,
                        "output_path": str(path),
                        "tokens_used": tokens_used,
                        "stage_paths": [str(stage_path) for stage_path in result.stage_paths],
                    }
                else:
                    active_prompt = _feedback_prompt(prompt, feedback)
                    response = active_prompt if getattr(client, "dry_run", False) else await client.generate(active_prompt)
                    body = response if isinstance(response, str) else response.text
                    tokens_used = 0 if isinstance(response, str) else response.tokens_used
                    path = write_result(spec.output_dir, item.filename, body)
                    payload = {
                        "status": "succeeded",
                        "attempts": attempt,
                        "output_path": str(path),
                        "tokens_used": tokens_used,
                    }
                update_item_state(
                    job_dir,
                    item,
                    payload,
                )
                append_jsonl(
                    job_dir / "events.jsonl",
                    {"event": "succeeded", "filename": item.filename, "attempt": attempt, "tokens_used": tokens_used},
                )
                return GenerationOutput("succeeded", tokens_used)
            except Exception as exc:
                if stop_token and stop_token.requested:
                    _cancel_item(job_dir, item, attempt)
                    return "cancelled"
                feedback = f"Previous attempt failed because {exc}."
                if attempt < MAX_ATTEMPTS:
                    append_jsonl(
                        job_dir / "events.jsonl",
                        {"event": "retrying", "filename": item.filename, "attempt": attempt + 1, "reason": str(exc)},
                    )
                    continue
                update_item_state(job_dir, item, {"status": "failed", "attempts": attempt, "error": str(exc)})
                append_jsonl(
                    job_dir / "errors.jsonl",
                    {"filename": item.filename, "attempts": attempt, "error": str(exc)},
                )
                return "failed"


def _feedback_prompt(prompt: str, feedback: str) -> str:
    return prompt if not feedback else f"{prompt}\n\n{feedback}"


def _cleanup_success(job_dir: Path, spec: JobSpec, state: dict[str, object]) -> None:
    if state["status"] != "completed" or state["failed"] or state["cancelled"]:
        return
    record_completed_job(spec, state)
    cleanup_job_dir(job_dir)


def _token_count(result: str | GenerationOutput) -> int:
    return 0 if isinstance(result, str) else result.tokens_used


def _cancel_item(job_dir: Path, item: JobItem, attempt: int) -> None:
    update_item_state(job_dir, item, {"status": "cancelled", "attempts": attempt})
    append_jsonl(job_dir / "events.jsonl", {"event": "cancelled", "filename": item.filename, "attempt": attempt})
