import json
import asyncio
from pathlib import Path

from codex_writer.api.generate import generate_batch
from codex_writer.jobs.model import JobItem, JobSpec
from codex_writer.queue.store import job_dir_for, load_job_state
from codex_writer.runner.batch import choose_concurrency
from codex_writer.sdk.result import GenerationOutput
from codex_writer.stop.token import StopToken


class FakeClient:
    async def generate(self, prompt: str) -> GenerationOutput:
        return GenerationOutput(f"OUT:{prompt}", 10)


def test_generate_batch_writes_outputs(tmp_path: Path) -> None:
    result = generate_batch(
        prompt_template="Write about {{topic}}.",
        items=[
            {"filename": "post-1.md", "topic": "testing"},
            {"filename": "post-2.md", "topic": "queues"},
        ],
        output_dir=tmp_path / "outputs",
        runtime_dir=tmp_path / "runtime",
        client=FakeClient(),
    )
    assert result.succeeded == 2
    assert result.tokens_used == 20
    assert (tmp_path / "outputs" / "post-1.md").read_text() == "OUT:Write about testing."
    assert not (tmp_path / "runtime" / "jobs" / result.job_id).exists()
    completed = tmp_path / "runtime" / "completed" / f"{result.job_id}.json"
    assert completed.exists()
    payload = json.loads(completed.read_text())
    assert payload["items"][0]["tokens_used"] == 10


def test_generate_batch_records_errors(tmp_path: Path) -> None:
    class BrokenClient:
        async def generate(self, prompt: str) -> str:
            raise RuntimeError(prompt)

    result = generate_batch(
        prompt_template="Write about {{topic}}.",
        items=[{"filename": "post-1.md", "topic": "errors"}],
        output_dir=tmp_path / "outputs",
        runtime_dir=tmp_path / "runtime",
        client=BrokenClient(),
    )
    assert result.failed == 1
    assert (tmp_path / "runtime" / "jobs" / result.job_id / "errors.jsonl").exists()


def test_generate_batch_retries_with_feedback(tmp_path: Path) -> None:
    class RetryClient:
        def __init__(self) -> None:
            self.prompts: list[str] = []

        async def generate(self, prompt: str) -> GenerationOutput:
            self.prompts.append(prompt)
            if len(self.prompts) == 1:
                raise RuntimeError("output.md was not created")
            return GenerationOutput("OUT:fixed", 25)

    client = RetryClient()
    result = generate_batch(
        prompt_template="Write about {{topic}}.",
        items=[{"filename": "post-1.md", "topic": "retry"}],
        output_dir=tmp_path / "outputs",
        runtime_dir=tmp_path / "runtime",
        client=client,
    )
    assert result.succeeded == 1
    assert result.tokens_used == 25
    assert "Previous attempt failed because output.md was not created." in client.prompts[1]
    assert (tmp_path / "outputs" / "post-1.md").read_text() == "OUT:fixed"


def test_choose_concurrency_caps_default_parallelism_at_four() -> None:
    assert choose_concurrency(item_count=10, requested=None) == 4


def test_run_batch_marks_stopped_item_cancelled(tmp_path: Path) -> None:
    token = StopToken()
    spec = JobSpec(
        job_id="job-stop",
        prompt_template="Write about {{topic}}.",
        output_dir=tmp_path / "outputs",
        runtime_dir=tmp_path / "runtime",
    )
    item = JobItem.from_dict({"filename": "post-1.md", "topic": "stop"})

    class StoppedClient:
        async def generate(self, prompt: str) -> str:
            token.request_stop()
            raise RuntimeError("terminated")

    async def run_test():
        from codex_writer.runner.batch import run_batch

        return await run_batch(spec, [item], StoppedClient(), token)

    result = asyncio.run(run_test())
    assert result.cancelled == 1
    state = load_job_state(job_dir_for(spec.runtime_dir, spec.job_id))
    assert state["status"] == "stopped"
    assert state["stop_requested"] is True
