from pathlib import Path

from codex_writer.validate.checks import run_checks
from codex_writer.validate.model import ValidationIssue, ValidationResult, ValidationSpec


def validate_file(path: Path, spec: ValidationSpec | None = None) -> ValidationResult:
    active_spec = spec or ValidationSpec()
    if not path.exists():
        return ValidationResult(
            valid=False,
            char_count=0,
            issues=[ValidationIssue("missing_file", f"file does not exist: {path}")],
            path=path,
        )
    text = path.read_text(encoding="utf-8").strip()
    return _result(text, active_spec, path)


def validate_text(text: str, spec: ValidationSpec | None = None) -> ValidationResult:
    active_spec = spec or ValidationSpec()
    return _result(text.strip(), active_spec, None)


def _result(text: str, spec: ValidationSpec, path: Path | None) -> ValidationResult:
    issues: list[ValidationIssue] = []
    if not text:
        issues.append(ValidationIssue("empty_text", "text is empty"))
    issues.extend(run_checks(text, spec))
    return ValidationResult(valid=not issues, char_count=len(text), issues=issues, path=path)
