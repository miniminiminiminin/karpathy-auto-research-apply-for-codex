import asyncio

import pytest

from codex_writer.api.generate import agenerate_batch, generate_batch


class FakeClient:
    async def generate(self, prompt: str) -> str:
        return f"OUT:{prompt}"


def test_agenerate_batch_runs_inside_event_loop(tmp_path) -> None:
    result = asyncio.run(
        agenerate_batch(
            prompt_template="Write about {{topic}}.",
            items=[{"filename": "post-1.md", "topic": "async"}],
            output_dir=tmp_path / "outputs",
            runtime_dir=tmp_path / "runtime",
            client=FakeClient(),
        )
    )
    assert result.succeeded == 1


def test_generate_batch_raises_inside_running_loop(tmp_path) -> None:
    async def run_test() -> None:
        with pytest.raises(RuntimeError):
            generate_batch(
                prompt_template="Write about {{topic}}.",
                items=[{"filename": "post-1.md", "topic": "async"}],
                output_dir=tmp_path / "outputs",
                runtime_dir=tmp_path / "runtime",
                dry_run=True,
            )

    asyncio.run(run_test())
