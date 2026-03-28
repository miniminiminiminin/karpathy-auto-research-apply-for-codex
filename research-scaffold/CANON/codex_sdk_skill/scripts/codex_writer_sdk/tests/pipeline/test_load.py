import json
from pathlib import Path

from codex_writer.pipeline.load import load_pipeline


def test_load_pipeline_resolves_stage_prompt_paths(tmp_path: Path) -> None:
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    (prompts / "01.md").write_text("one", encoding="utf-8")
    (prompts / "02.md").write_text("two", encoding="utf-8")
    pipeline_path = tmp_path / "pipeline.json"
    pipeline_path.write_text(
        json.dumps(
            {
                "name": "book-chapter",
                "mode": "sequential",
                "final_output": "final.md",
                "stages": [
                    {
                        "id": "architect",
                        "prompt_file": "prompts/01.md",
                        "output_file": "01-architect.md",
                        "use_previous_output": False,
                    },
                    {
                        "id": "writer",
                        "prompt_file": "prompts/02.md",
                        "output_file": "02-writer.md",
                        "use_previous_output": True,
                    },
                ],
            }
        ),
        encoding="utf-8",
    )

    spec = load_pipeline(pipeline_path)

    assert spec.name == "book-chapter"
    assert spec.final_output == "final.md"
    assert len(spec.stages) == 2
    assert spec.stages[0].prompt_path == prompts / "01.md"
    assert spec.stages[1].use_previous_output is True


def test_load_pipeline_allows_prompt_paths_relative_to_workspace_root(tmp_path: Path) -> None:
    prompts = tmp_path / "prompts"
    prompts.mkdir()
    (prompts / "01.md").write_text("one", encoding="utf-8")
    pipeline_dir = tmp_path / "pipelines"
    pipeline_dir.mkdir()
    pipeline_path = pipeline_dir / "book.json"
    pipeline_path.write_text(
        json.dumps(
            {
                "name": "book-chapter",
                "final_output": "final.md",
                "stages": [
                    {
                        "id": "architect",
                        "prompt_file": "prompts/01.md",
                        "output_file": "01-architect.md",
                    }
                ],
            }
        ),
        encoding="utf-8",
    )

    spec = load_pipeline(pipeline_path)

    assert spec.stages[0].prompt_path == prompts / "01.md"
