from xml.etree import ElementTree as ET

from codex_writer.validate.model import ValidationIssue, ValidationSpec


def run_checks(text: str, spec: ValidationSpec) -> list[ValidationIssue]:
    issues: list[ValidationIssue] = []
    issues.extend(_length_issues(text, spec))
    issues.extend(_required_issues(text, spec.required_substrings))
    issues.extend(_forbidden_issues(text, spec.forbidden_substrings))
    if spec.expect_xml:
        issue = _xml_issue(text)
        if issue is not None:
            issues.append(issue)
    return issues


def _length_issues(text: str, spec: ValidationSpec) -> list[ValidationIssue]:
    char_count = len(text)
    issues: list[ValidationIssue] = []
    if spec.min_chars is not None and char_count < spec.min_chars:
        issues.append(
            ValidationIssue("too_short", f"text has {char_count} chars; minimum is {spec.min_chars}")
        )
    if spec.max_chars is not None and char_count > spec.max_chars:
        issues.append(
            ValidationIssue("too_long", f"text has {char_count} chars; maximum is {spec.max_chars}")
        )
    return issues


def _required_issues(text: str, required: tuple[str, ...]) -> list[ValidationIssue]:
    return [
        ValidationIssue("missing_required_substring", f"missing required substring: {needle}")
        for needle in required
        if needle not in text
    ]


def _forbidden_issues(text: str, forbidden: tuple[str, ...]) -> list[ValidationIssue]:
    return [
        ValidationIssue("contains_forbidden_substring", f"contains forbidden substring: {needle}")
        for needle in forbidden
        if needle in text
    ]


def _xml_issue(text: str) -> ValidationIssue | None:
    try:
        ET.fromstring(text)
    except ET.ParseError as exc:
        return ValidationIssue("invalid_xml", str(exc))
    return None
