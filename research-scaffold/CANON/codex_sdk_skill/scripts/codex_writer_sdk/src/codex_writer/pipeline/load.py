import json
from pathlib import Path

from codex_writer.pipeline.model import PipelineSpec, StageSpec


def load_pipeline(path: Path) -> PipelineSpec:
    payload = json.loads(path.read_text(encoding="utf-8"))
    return _from_payload(payload, path.parent)


def load_pipeline_payload(payload: dict[str, object]) -> PipelineSpec:
    return _from_payload(payload, Path.cwd())


def _from_payload(payload: dict[str, object], base_dir: Path) -> PipelineSpec:
    stages = tuple(
        StageSpec(
            id=str(stage["id"]),
            prompt_path=_resolve_prompt_path(base_dir, str(stage["prompt_file"])),
            output_file=str(stage["output_file"]),
            use_previous_output=bool(stage.get("use_previous_output", True)),
        )
        for stage in payload["stages"]
    )
    return PipelineSpec(
        name=str(payload["name"]),
        mode=str(payload.get("mode", "sequential")),
        final_output=str(payload.get("final_output", "final.md")),
        stages=stages,
    )


def _resolve_prompt_path(base_dir: Path, prompt_file: str) -> Path:
    path = Path(prompt_file)
    if path.is_absolute():
        return path
    direct = (base_dir / path).resolve()
    if direct.exists():
        return direct
    sibling = (base_dir.parent / path).resolve()
    return sibling
