from codex_writer.jobs.model import JobItem


def test_job_item_requires_filename() -> None:
    item = JobItem.from_dict({"filename": "post-1.md", "topic": "AI"})
    assert item.filename == "post-1.md"
    assert item.variables["topic"] == "AI"
