import asyncio
from pathlib import Path

from codex_writer.config.load import load_plain_config
from codex_writer.input.load import load_items
from codex_writer.jobs.model import BatchResult, JobItem, JobSpec
from codex_writer.pipeline.load import load_pipeline
from codex_writer.queue.store import make_job_id
from codex_writer.runner.batch import run_batch
from codex_writer.sdk.client import CodexClient


class DryRunClient:
    dry_run = True

    async def generate(self, prompt: str) -> str:
        return prompt


def generate_batch(
    prompt_template: str,
    items: list[dict[str, object]] | list[JobItem],
    output_dir: Path,
    runtime_dir: Path | None = None,
    client: object | None = None,
    concurrency: int | None = None,
    dry_run: bool = False,
) -> BatchResult:
    _ensure_sync_context()
    return asyncio.run(
        agenerate_batch(prompt_template, items, output_dir, runtime_dir, client, concurrency, dry_run)
    )


async def agenerate_batch(
    prompt_template: str,
    items: list[dict[str, object]] | list[JobItem],
    output_dir: Path,
    runtime_dir: Path | None = None,
    client: object | None = None,
    concurrency: int | None = None,
    dry_run: bool = False,
) -> BatchResult:
    config = load_plain_config(Path(runtime_dir) if runtime_dir is not None else None)
    job_items = [_to_job_item(item) for item in items]
    spec = JobSpec(
        job_id=make_job_id(),
        prompt_template=prompt_template,
        output_dir=Path(output_dir),
        runtime_dir=config.runtime_dir,
        concurrency=concurrency,
        dry_run=dry_run,
    )
    active_client = client or (DryRunClient() if dry_run else CodexClient(config))
    return await run_batch(spec, job_items, active_client)


def generate_one(
    prompt_template: str,
    variables: dict[str, object],
    output_dir: Path,
    runtime_dir: Path | None = None,
    client: object | None = None,
    dry_run: bool = False,
) -> BatchResult:
    _ensure_sync_context()
    return asyncio.run(agenerate_one(prompt_template, variables, output_dir, runtime_dir, client, dry_run))


def generate_pipeline(
    pipeline: Path,
    manifest: Path,
    output_dir: Path,
    runtime_dir: Path | None = None,
    client: object | None = None,
    concurrency: int | None = None,
    dry_run: bool = False,
) -> BatchResult:
    _ensure_sync_context()
    return asyncio.run(
        agenerate_pipeline(pipeline, manifest, output_dir, runtime_dir, client, concurrency, dry_run)
    )


async def agenerate_pipeline(
    pipeline: Path,
    manifest: Path,
    output_dir: Path,
    runtime_dir: Path | None = None,
    client: object | None = None,
    concurrency: int | None = None,
    dry_run: bool = False,
) -> BatchResult:
    config = load_plain_config(Path(runtime_dir) if runtime_dir is not None else None)
    spec = JobSpec(
        job_id=make_job_id(),
        prompt_template="",
        output_dir=Path(output_dir),
        runtime_dir=config.runtime_dir,
        concurrency=concurrency,
        dry_run=dry_run,
        pipeline=load_pipeline(Path(pipeline)).to_dict(),
    )
    active_client = client or (DryRunClient() if dry_run else CodexClient(config))
    return await run_batch(spec, load_items(Path(manifest)), active_client)


async def agenerate_one(
    prompt_template: str,
    variables: dict[str, object],
    output_dir: Path,
    runtime_dir: Path | None = None,
    client: object | None = None,
    dry_run: bool = False,
) -> BatchResult:
    item = {"filename": str(variables["filename"]), **variables}
    return await agenerate_batch(prompt_template, [item], output_dir, runtime_dir, client, 1, dry_run)


def _to_job_item(item: dict[str, object] | JobItem) -> JobItem:
    return item if isinstance(item, JobItem) else JobItem.from_dict(item)


def _ensure_sync_context() -> None:
    try:
        asyncio.get_running_loop()
    except RuntimeError:
        return
    raise RuntimeError("generate_batch cannot run inside an active event loop; use agenerate_batch instead")
