from pathlib import Path

from codex_writer.output.write import write_result


def test_write_result_creates_article_file(tmp_path: Path) -> None:
    path = write_result(tmp_path, "post-1.md", "# Title")
    assert path.read_text() == "# Title"
