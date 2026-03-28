from dataclasses import dataclass
from pathlib import Path
from textwrap import dedent

from codex_writer.settings.plain import default_plain_settings


@dataclass(slots=True)
class PlainConfig:
    profile: str = "plain"
    model: str = "gpt-5.4"
    reasoning_effort: str = "high"
    runtime_dir: Path = Path("runtime")


def load_plain_config(runtime_dir: Path | None = None) -> PlainConfig:
    config = PlainConfig()
    if runtime_dir is not None:
        config.runtime_dir = runtime_dir
    return config


def write_plain_config(codex_home: Path, config: PlainConfig | None = None) -> Path:
    active = config or load_plain_config()
    codex_home.mkdir(parents=True, exist_ok=True)
    instructions_path = codex_home / "instructions.md"
    instructions_path.write_text(default_plain_settings().instructions, encoding="utf-8")
    config_path = codex_home / "config.toml"
    config_path.write_text(_render_plain_config(active, instructions_path), encoding="utf-8")
    return config_path


def _render_plain_config(config: PlainConfig, instructions_path: Path) -> str:
    settings = default_plain_settings()
    return dedent(
        f"""
        model = "{config.model}"
        model_reasoning_effort = "{config.reasoning_effort}"
        personality = "{settings.personality}"
        web_search = "{settings.web_search}"
        project_doc_max_bytes = {settings.project_doc_max_bytes}
        project_doc_fallback_filenames = []
        model_instructions_file = "{_toml_path(instructions_path)}"

        [history]
        persistence = "{settings.history_persistence}"
        """
    ).strip() + "\n"


def _toml_path(path: Path) -> str:
    return str(path).replace("\\", "\\\\").replace('"', '\\"')
