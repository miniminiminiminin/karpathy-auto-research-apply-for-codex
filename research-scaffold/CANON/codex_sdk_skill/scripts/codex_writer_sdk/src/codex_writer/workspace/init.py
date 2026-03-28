import shutil
from pathlib import Path


def initialize_workspace(workspace: Path, preset: str, skill_root: Path | None = None) -> Path:
    root = skill_root or _skill_root()
    preset_root = root / "presets" / preset
    template_root = root / "scripts" / "templates"
    sdk_root = root / "scripts" / "codex_writer_sdk"
    workspace.mkdir(parents=True, exist_ok=True)

    for name in ("prompts", "pipelines", "manifests", "shared"):
        source = preset_root / name
        if source.exists():
            shutil.copytree(source, workspace / name, dirs_exist_ok=True)

    shutil.copytree(sdk_root, workspace / "sdk", dirs_exist_ok=True)
    (workspace / "outputs").mkdir(parents=True, exist_ok=True)
    (workspace / "runtime").mkdir(parents=True, exist_ok=True)
    (workspace / "scripts").mkdir(parents=True, exist_ok=True)

    run_template = template_root / "run_pipeline.py"
    if run_template.exists():
        shutil.copy2(run_template, workspace / "scripts" / "run_pipeline.py")
    readme_template = template_root / "workspace_README.md"
    if readme_template.exists():
        shutil.copy2(readme_template, workspace / "README.md")
    elif (preset_root / "README.md").exists():
        shutil.copy2(preset_root / "README.md", workspace / "README.md")

    return workspace


def _skill_root() -> Path:
    return Path(__file__).resolve().parents[5]
