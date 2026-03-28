import importlib
from pathlib import Path

from codex_writer.jobs.model import BatchResult


def test_build_parser_has_workspace_and_pipeline_commands() -> None:
    cli = importlib.import_module("codex_writer.cli.main")
    parser = cli.build_parser()
    workspace = parser.parse_args(["workspace", "init", "--workspace", "job"])
    pipeline = parser.parse_args(["pipeline", "run", "--pipeline", "pipe.json", "--manifest", "items.jsonl"])
    assert workspace.command == "workspace"
    assert pipeline.command == "pipeline"


def test_main_initializes_workspace(monkeypatch, tmp_path: Path) -> None:
    cli = importlib.import_module("codex_writer.cli.main")
    called: dict[str, object] = {}

    def fake_initialize_workspace(workspace: Path, preset: str, skill_root: Path | None = None) -> Path:
        called["workspace"] = workspace
        called["preset"] = preset
        return workspace

    monkeypatch.setattr(cli, "initialize_workspace", fake_initialize_workspace)
    code = cli.main(["workspace", "init", "--workspace", str(tmp_path / "job"), "--preset", "book-chapter"])

    assert code == 0
    assert called["preset"] == "book-chapter"


def test_main_runs_pipeline(monkeypatch, tmp_path: Path) -> None:
    cli = importlib.import_module("codex_writer.cli.main")
    called: dict[str, object] = {}

    def fake_generate_pipeline(**kwargs):
        called.update(kwargs)
        return BatchResult("job-1", 1, 1, 0, 0, 5)

    monkeypatch.setattr(cli, "generate_pipeline", fake_generate_pipeline)
    code = cli.main(
        [
            "pipeline",
            "run",
            "--pipeline",
            str(tmp_path / "book.json"),
            "--manifest",
            str(tmp_path / "chapters.jsonl"),
            "--output-dir",
            str(tmp_path / "outputs"),
            "--runtime-dir",
            str(tmp_path / "runtime"),
        ]
    )

    assert code == 0
    assert called["pipeline"] == tmp_path / "book.json"
    assert called["manifest"] == tmp_path / "chapters.jsonl"
