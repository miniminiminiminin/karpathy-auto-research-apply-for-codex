import importlib.util
from pathlib import Path


def _load_init_module() -> object:
    path = Path(__file__).resolve().parents[4] / "scripts" / "init_workspace.py"
    spec = importlib.util.spec_from_file_location("skill_init_workspace", path)
    assert spec is not None
    assert spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_init_workspace_copies_preset_and_sdk_to_arbitrary_path(tmp_path: Path) -> None:
    module = _load_init_module()
    skill_root = tmp_path / "skill-root"
    preset_root = skill_root / "presets" / "book-chapter"
    sdk_root = skill_root / "scripts" / "codex_writer_sdk"
    template_root = skill_root / "scripts" / "templates"
    (preset_root / "prompts").mkdir(parents=True)
    (preset_root / "pipelines").mkdir(parents=True)
    (preset_root / "manifests").mkdir(parents=True)
    (preset_root / "shared").mkdir(parents=True)
    (sdk_root / "src").mkdir(parents=True)
    template_root.mkdir(parents=True)
    (preset_root / "prompts" / "01-architect.md").write_text("prompt", encoding="utf-8")
    (preset_root / "pipelines" / "book-chapter.json").write_text("{}", encoding="utf-8")
    (preset_root / "manifests" / "chapters.jsonl").write_text("", encoding="utf-8")
    (preset_root / "shared" / "style-guide.md").write_text("style", encoding="utf-8")
    (preset_root / "README.md").write_text("preset readme", encoding="utf-8")
    (sdk_root / "pyproject.toml").write_text("[project]\nname='x'\nversion='0.0.0'\n", encoding="utf-8")
    (template_root / "run_pipeline.py").write_text("print('run')\n", encoding="utf-8")
    (template_root / "workspace_README.md").write_text("workspace", encoding="utf-8")
    workspace = tmp_path / "anywhere" / "job-root"

    module.initialize_workspace(workspace=workspace, preset="book-chapter", skill_root=skill_root)

    assert (workspace / "prompts" / "01-architect.md").exists()
    assert (workspace / "pipelines" / "book-chapter.json").exists()
    assert (workspace / "manifests" / "chapters.jsonl").exists()
    assert (workspace / "shared" / "style-guide.md").exists()
    assert (workspace / "scripts" / "run_pipeline.py").exists()
    assert (workspace / "sdk" / "pyproject.toml").exists()
    assert (workspace / "outputs").is_dir()
    assert (workspace / "runtime").is_dir()
