from pathlib import Path

from codex_writer.validate import ValidationSpec, validate_file, validate_text


def test_validate_file_flags_missing_file(tmp_path: Path) -> None:
    result = validate_file(tmp_path / "missing.txt")
    assert result.valid is False
    assert result.char_count == 0
    assert result.issues[0].code == "missing_file"


def test_validate_text_checks_length_and_substrings() -> None:
    spec = ValidationSpec(
        min_chars=10,
        max_chars=20,
        required_substrings=("alpha",),
        forbidden_substrings=("omega",),
    )
    result = validate_text("alpha beta", spec)
    assert result.valid is True
    assert result.char_count == 10
    assert result.issues == []


def test_validate_text_collects_multiple_failures() -> None:
    spec = ValidationSpec(
        min_chars=5,
        max_chars=8,
        required_substrings=("need",),
        forbidden_substrings=("bad",),
    )
    result = validate_text("bad", spec)
    assert result.valid is False
    codes = [issue.code for issue in result.issues]
    assert codes == ["too_short", "missing_required_substring", "contains_forbidden_substring"]


def test_validate_text_parses_xml_when_requested() -> None:
    result = validate_text("<article><body>ok</body></article>", ValidationSpec(expect_xml=True))
    assert result.valid is True


def test_validate_text_reports_invalid_xml() -> None:
    result = validate_text("<article><body></article>", ValidationSpec(expect_xml=True))
    assert result.valid is False
    assert result.issues[0].code == "invalid_xml"
