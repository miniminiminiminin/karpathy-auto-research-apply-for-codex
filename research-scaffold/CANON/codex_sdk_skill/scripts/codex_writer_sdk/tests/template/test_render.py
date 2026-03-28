from codex_writer.template.render import render_prompt


def test_render_prompt_replaces_placeholders() -> None:
    prompt = render_prompt(
        "Write about {{topic}} in {{tone}} tone.",
        {"topic": "robots", "tone": "calm"},
    )
    assert prompt == "Write about robots in calm tone."
