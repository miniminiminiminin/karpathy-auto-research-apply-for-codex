import asyncio
from pathlib import Path

from codex_writer.sdk.client import CodexClient, _extract_text, _extract_tokens


def test_extract_text_reads_nested_agent_messages() -> None:
    stdout = '\n'.join(
        [
            '{"type":"thread.started","thread_id":"x"}',
            '{"type":"item.completed","item":{"type":"agent_message","text":"hello"}}',
        ]
    )
    assert _extract_text(stdout) == "hello"


def test_extract_tokens_reads_footer_count() -> None:
    stderr = "codex\n업무가 완료되었습니다.\ntokens used\n7,633\n"
    assert _extract_tokens("", stderr) == 7633


def test_client_uses_isolated_workdir(monkeypatch) -> None:
    captured = {}

    class FakeProcess:
        returncode = 0

        async def communicate(self) -> tuple[bytes, bytes]:
            payload = b'{"type":"item.completed","item":{"type":"agent_message","text":"ok"}}\n'
            return payload, b"tokens used\n44\n"

    async def fake_exec(*args, **kwargs):
        captured["cwd"] = kwargs["cwd"]
        captured["env"] = kwargs["env"]
        config_path = Path(kwargs["env"]["CODEX_HOME"]) / "config.toml"
        captured["config_text"] = config_path.read_text()
        instructions_line = next(
            line for line in captured["config_text"].splitlines() if line.startswith("model_instructions_file")
        )
        instructions_path = Path(instructions_line.split('"')[1])
        captured["instructions_text"] = instructions_path.read_text()
        Path(kwargs["cwd"], "output.md").write_text("# article")
        return FakeProcess()

    monkeypatch.setattr("codex_writer.sdk.client.asyncio.create_subprocess_exec", fake_exec)

    async def run_test() -> None:
        client = CodexClient()
        result = await client.generate("hello")
        assert result.text == "# article"
        assert result.tokens_used == 44

    asyncio.run(run_test())
    assert Path(captured["cwd"]).resolve() != Path.cwd().resolve()
    config_text = captured["config_text"]
    assert 'web_search = "disabled"' in config_text
    assert '[history]\npersistence = "none"' in config_text
    assert "model_instructions_file" in config_text
    assert captured["instructions_text"].strip()


def test_client_copies_auth_files_into_isolated_home(monkeypatch, tmp_path: Path) -> None:
    source_home = tmp_path / "source-home"
    source_home.mkdir()
    (source_home / "auth.json").write_text('{"token":"a"}')
    (source_home / ".credentials.json").write_text('{"creds":"b"}')
    monkeypatch.setenv("CODEX_HOME", str(source_home))
    captured = {}

    class FakeProcess:
        returncode = 0

        async def communicate(self) -> tuple[bytes, bytes]:
            return b"", b""

    async def fake_exec(*args, **kwargs):
        temp_home = Path(kwargs["env"]["CODEX_HOME"])
        captured["auth"] = (temp_home / "auth.json").read_text()
        captured["creds"] = (temp_home / ".credentials.json").read_text()
        Path(kwargs["cwd"], "output.md").write_text("# article")
        return FakeProcess()

    monkeypatch.setattr("codex_writer.sdk.client.asyncio.create_subprocess_exec", fake_exec)

    async def run_test() -> None:
        client = CodexClient()
        result = await client.generate("hello")
        assert result.text == "# article"

    asyncio.run(run_test())
    assert captured["auth"] == '{"token":"a"}'
    assert captured["creds"] == '{"creds":"b"}'


def test_client_registers_and_cleans_up_active_process(monkeypatch) -> None:
    handles = []

    class FakeProcess:
        pid = 321

        def __init__(self) -> None:
            self.returncode = None

        async def communicate(self) -> tuple[bytes, bytes]:
            self.returncode = 0
            return b"", b"tokens used\n9\n"

        def terminate(self) -> None:
            self.returncode = -15

        def kill(self) -> None:
            self.returncode = -9

    async def fake_exec(*args, **kwargs):
        Path(kwargs["cwd"], "output.md").write_text("# article")
        return FakeProcess()

    monkeypatch.setattr("codex_writer.sdk.client.asyncio.create_subprocess_exec", fake_exec)

    async def run_test() -> None:
        client = CodexClient(on_process=handles.append)
        result = await client.generate("hello")
        assert result.text == "# article"
        assert result.tokens_used == 9

    asyncio.run(run_test())
    assert len(handles) == 1
    assert handles[0].pid == 321
    assert handles[0].is_running() is False
