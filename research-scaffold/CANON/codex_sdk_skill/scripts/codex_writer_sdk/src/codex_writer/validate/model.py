from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ValidationSpec:
    min_chars: int | None = None
    max_chars: int | None = None
    required_substrings: tuple[str, ...] = ()
    forbidden_substrings: tuple[str, ...] = ()
    expect_xml: bool = False


@dataclass(frozen=True, slots=True)
class ValidationIssue:
    code: str
    message: str


@dataclass(frozen=True, slots=True)
class ValidationResult:
    valid: bool
    char_count: int
    issues: list[ValidationIssue] = field(default_factory=list)
    path: Path | None = None
