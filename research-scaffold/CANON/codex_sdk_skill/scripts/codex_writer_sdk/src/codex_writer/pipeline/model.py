from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class StageSpec:
    id: str
    prompt_path: Path
    output_file: str
    use_previous_output: bool = True

    def to_dict(self) -> dict[str, object]:
        return {
            "id": self.id,
            "prompt_file": str(self.prompt_path),
            "output_file": self.output_file,
            "use_previous_output": self.use_previous_output,
        }


@dataclass(slots=True)
class PipelineSpec:
    name: str
    mode: str
    final_output: str
    stages: tuple[StageSpec, ...]

    def to_dict(self) -> dict[str, object]:
        return {
            "name": self.name,
            "mode": self.mode,
            "final_output": self.final_output,
            "stages": [stage.to_dict() for stage in self.stages],
        }


@dataclass(slots=True)
class PipelineRunResult:
    final_path: Path
    stage_paths: list[Path]
    tokens_used: int = 0
