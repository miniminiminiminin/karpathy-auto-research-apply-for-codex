from pathlib import Path

from codex_writer.config.load import write_plain_config
from codex_writer.settings.plain import default_plain_settings


def test_default_plain_settings_live_in_settings_package() -> None:
    settings = default_plain_settings()
    assert settings.model == "gpt-5.4"
    assert settings.reasoning_effort == "high"
    assert "plain content-generation assistant" in settings.instructions


def test_write_plain_config_uses_settings_defaults(tmp_path: Path) -> None:
    config_path = write_plain_config(tmp_path)
    config_text = config_path.read_text(encoding="utf-8")
    instructions_text = (tmp_path / "instructions.md").read_text(encoding="utf-8")
    assert 'model = "gpt-5.4"' in config_text
    assert 'model_reasoning_effort = "high"' in config_text
    assert "plain content-generation assistant" in instructions_text
