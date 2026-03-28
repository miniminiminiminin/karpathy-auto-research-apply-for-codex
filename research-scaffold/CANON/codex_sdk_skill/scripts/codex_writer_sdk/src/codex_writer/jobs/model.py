from dataclasses import dataclass
from pathlib import Path


@dataclass(slots=True)
class JobItem:
    filename: str
    variables: dict[str, object]

    @classmethod
    def from_dict(cls, payload: dict[str, object]) -> "JobItem":
        filename = str(payload["filename"]).strip()
        if not filename:
            raise ValueError("filename is required")
        variables = {k: v for k, v in payload.items() if k != "filename"}
        return cls(filename=filename, variables=variables)


@dataclass(slots=True)
class JobSpec:
    job_id: str
    output_dir: Path
    runtime_dir: Path
    prompt_template: str = ""
    concurrency: int | None = None
    dry_run: bool = False
    pipeline: dict[str, object] | None = None


@dataclass(slots=True)
class BatchResult:
    job_id: str
    item_count: int
    succeeded: int
    failed: int
    cancelled: int
    tokens_used: int = 0
