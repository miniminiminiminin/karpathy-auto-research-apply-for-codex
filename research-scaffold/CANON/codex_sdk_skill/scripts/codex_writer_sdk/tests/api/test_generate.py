from codex_writer.api.generate import generate_batch


def test_generate_batch_accepts_items_and_output_dir(tmp_path) -> None:
    result = generate_batch(
        prompt_template="Write about {{topic}}.",
        items=[{"filename": "post-1.md", "topic": "testing"}],
        output_dir=tmp_path,
        runtime_dir=tmp_path / "runtime",
        dry_run=True,
    )
    assert result.item_count == 1
