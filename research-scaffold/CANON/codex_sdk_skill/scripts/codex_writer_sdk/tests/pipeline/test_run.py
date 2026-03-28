import asyncio
from pathlib import Path

from codex_writer.jobs.model import JobItem
from codex_writer.pipeline.model import PipelineSpec, StageSpec
from codex_writer.pipeline.run import run_pipeline_for_item
from codex_writer.sdk.result import GenerationOutput


class FakeClient:
    def __init__(self) -> None:
        self.prompts: list[str] = []

    async def generate(self, prompt: str) -> GenerationOutput:
        self.prompts.append(prompt)
        return GenerationOutput(text=f"OUT:{len(self.prompts)}", tokens_used=7)


def test_run_pipeline_for_item_writes_stage_outputs_and_final(tmp_path: Path) -> None:
    prompt_dir = tmp_path / "prompts"
    prompt_dir.mkdir()
    (prompt_dir / "01.md").write_text("Plan {{chapter_title}}", encoding="utf-8")
    (prompt_dir / "02.md").write_text("Write from {{previous_output}}", encoding="utf-8")
    spec = PipelineSpec(
        name="book",
        mode="sequential",
        final_output="final.md",
        stages=(
            StageSpec("architect", prompt_dir / "01.md", "01-architect.md", False),
            StageSpec("writer", prompt_dir / "02.md", "02-writer.md", True),
        ),
    )
    item = JobItem.from_dict({"filename": "chapter-01/final.md", "chapter_title": "원칙"})
    client = FakeClient()

    result = asyncio.run(run_pipeline_for_item(spec, item, tmp_path / "outputs", client))

    assert result.final_path == tmp_path / "outputs" / "chapter-01" / "final.md"
    assert result.stage_paths[0] == tmp_path / "outputs" / "chapter-01" / "01-architect.md"
    assert result.stage_paths[1] == tmp_path / "outputs" / "chapter-01" / "02-writer.md"
    assert result.final_path.read_text(encoding="utf-8") == "OUT:2"
    assert "Plan 원칙" in client.prompts[0]
    assert "Write from OUT:1" in client.prompts[1]
