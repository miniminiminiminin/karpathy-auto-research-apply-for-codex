import importlib
import json
from pathlib import Path

from codex_writer.cli.main import build_parser, main


def test_build_parser_has_generate_command() -> None:
    parser = build_parser()
    args = parser.parse_args(["generate"])
    assert args.command == "generate"


def test_main_starts_daemon(monkeypatch, tmp_path: Path) -> None:
    cli_module = importlib.import_module("codex_writer.cli.main")
    called = {}

    def fake_run_daemon(runtime_dir: Path, socket_path: Path) -> None:
        called["runtime_dir"] = runtime_dir
        called["socket_path"] = socket_path

    monkeypatch.setattr(cli_module, "run_daemon", fake_run_daemon)
    code = main(
        [
            "daemon",
            "--socket-path",
            str(tmp_path / "daemon.sock"),
            "--runtime-dir",
            str(tmp_path / "runtime"),
            "start",
        ]
    )
    assert code == 0
    assert called["runtime_dir"] == tmp_path / "runtime"


def test_main_requests_job_report(monkeypatch, capsys) -> None:
    cli_module = importlib.import_module("codex_writer.cli.main")

    class FakeClient:
        def __init__(self, socket_path: Path) -> None:
            self.socket_path = socket_path

        def request(self, command: str, payload: dict[str, object]) -> dict[str, object]:
            assert command == "report"
            assert payload == {"job_id": "job-1"}
            return {"job_id": "job-1", "tokens_used": 10}

    monkeypatch.setattr(cli_module, "DaemonClient", FakeClient)
    code = main(["job", "report", "job-1"])
    assert code == 0
    assert json.loads(capsys.readouterr().out)["tokens_used"] == 10


def test_main_validates_file(monkeypatch, tmp_path: Path, capsys) -> None:
    cli_module = importlib.import_module("codex_writer.cli.main")
    path = tmp_path / "article.xml"
    path.write_text("<article/>", encoding="utf-8")

    class FakeResult:
        valid = True
        char_count = 10
        issues: list[object] = []

        def __init__(self) -> None:
            self.path = path

    def fake_validate_file(target: Path, spec) -> FakeResult:
        assert target == path
        assert spec.expect_xml is True
        return FakeResult()

    monkeypatch.setattr(cli_module, "validate_file", fake_validate_file)
    code = main(["validate", str(path), "--expect-xml", "--min-chars", "5"])
    assert code == 0
    assert json.loads(capsys.readouterr().out)["valid"] is True
