from pathlib import Path


def write_result(output_dir: Path, filename: str, text: str) -> Path:
    path = output_dir / filename
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return path


def resolve_pipeline_final_path(filename: str, final_output: str) -> Path:
    path = Path(filename)
    if path.name == final_output:
        return path
    if path.suffix:
        return path.parent / final_output
    return path / final_output


def write_stage_result(output_dir: Path, filename: str, final_output: str, stage_filename: str, text: str) -> Path:
    final_path = resolve_pipeline_final_path(filename, final_output)
    return write_result(output_dir, str(final_path.parent / stage_filename), text)
