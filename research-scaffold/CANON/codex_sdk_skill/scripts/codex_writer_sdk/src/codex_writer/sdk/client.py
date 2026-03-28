import asyncio
import json
import os
import re
import shutil
from collections.abc import Callable
from pathlib import Path
from tempfile import TemporaryDirectory

from codex_writer.config.load import PlainConfig, load_plain_config, write_plain_config
from codex_writer.sdk.process import ActiveProcess
from codex_writer.sdk.result import GenerationOutput


class CodexClient:
    def __init__(
        self,
        config: PlainConfig | None = None,
        executable: str = "codex",
        on_process: Callable[[ActiveProcess], None] | None = None,
    ) -> None:
        self.config = config or load_plain_config()
        self.executable = executable
        self.on_process = on_process

    async def generate(self, prompt: str) -> GenerationOutput:
        with TemporaryDirectory(prefix="codex-writer-") as temp_dir:
            sandbox_root = Path(temp_dir)
            codex_home = sandbox_root / "codex-home"
            workspace = sandbox_root / "workspace"
            workspace.mkdir(parents=True, exist_ok=True)
            write_plain_config(codex_home, self.config)
            _copy_auth_files(codex_home)
            process = await asyncio.create_subprocess_exec(
                *self._command(prompt),
                stdout=asyncio.subprocess.PIPE,
                stderr=asyncio.subprocess.PIPE,
                cwd=str(workspace),
                env=_build_env(codex_home),
            )
            active_process = ActiveProcess(process)
            if self.on_process is not None:
                self.on_process(active_process)
            try:
                stdout, stderr = await process.communicate()
            finally:
                active_process.close()
            return _read_output(workspace, stdout.decode(), stderr.decode(), process.returncode)

    def _command(self, prompt: str) -> list[str]:
        return [
            self.executable,
            "exec",
            "--full-auto",
            "--ephemeral",
            "--skip-git-repo-check",
            "--output-last-message",
            "last_message.txt",
            _file_prompt(prompt),
        ]


def _extract_text(stdout: str) -> str:
    lines = [line for line in stdout.splitlines() if line.strip()]
    messages: list[str] = []
    for line in lines:
        try:
            payload = json.loads(line)
        except json.JSONDecodeError:
            messages.append(line)
            continue
        msg = payload.get("msg", {})
        if isinstance(msg, dict) and msg.get("type") == "agent_message":
            text = msg.get("message")
            if isinstance(text, str):
                messages.append(text)
        item = payload.get("item", {})
        if isinstance(item, dict) and item.get("type") == "agent_message":
            text = item.get("text")
            if isinstance(text, str):
                messages.append(text)
    return messages[-1] if messages else stdout.strip()


def _build_env(codex_home: Path) -> dict[str, str]:
    env = os.environ.copy()
    env["CODEX_HOME"] = str(codex_home)
    return env


def _copy_auth_files(codex_home: Path) -> None:
    source_home = Path(os.environ.get("CODEX_HOME", Path.home() / ".codex"))
    for name in ("auth.json", ".credentials.json"):
        source = source_home / name
        if source.exists():
            shutil.copy2(source, codex_home / name)


def _file_prompt(prompt: str) -> str:
    return "\n".join(
        [
            "Write the final answer to output.md in the current working directory.",
            "Do not ask clarifying questions.",
            "Do not wait for confirmation.",
            "Overwrite output.md if it already exists.",
            "Return only a short confirmation after the file is written.",
            "",
            "User request:",
            prompt,
        ]
    )


def _read_output(workspace: Path, stdout: str, stderr: str, returncode: int) -> GenerationOutput:
    output_path = workspace / "output.md"
    if returncode != 0:
        raise RuntimeError(_diagnostic_message("codex exec failed", workspace, stdout, stderr))
    if not output_path.exists():
        raise RuntimeError("output.md was not created")
    body = output_path.read_text(encoding="utf-8").strip()
    if not body:
        raise RuntimeError("output.md was empty")
    if _looks_interactive(body):
        raise RuntimeError("output.md contained interactive follow-up instead of the article")
    return GenerationOutput(text=body, tokens_used=_extract_tokens(stdout, stderr))


def _diagnostic_message(prefix: str, workspace: Path, stdout: str, stderr: str) -> str:
    last_path = workspace / "last_message.txt"
    last_message = last_path.read_text(encoding="utf-8").strip() if last_path.exists() else ""
    detail = last_message or _extract_text(stdout) or stderr.strip()
    return f"{prefix}: {detail}".rstrip(": ")


def _looks_interactive(body: str) -> bool:
    lowered = body.lower()
    markers = (
        "원하시는 번호",
        "질문 1개",
        "답이 없으면",
        "어떤 실전 사례",
        "which option",
        "please choose",
        "what would you like",
    )
    if any(marker.lower() in lowered for marker in markers):
        return True
    return len(body) < 120 and body.rstrip().endswith("?")


def _extract_tokens(stdout: str, stderr: str) -> int:
    pattern = re.compile(r"tokens used\s*\n([0-9][0-9,]*)", re.IGNORECASE)
    for text in (stderr, stdout):
        match = pattern.search(text)
        if match:
            return int(match.group(1).replace(",", ""))
    return 0
