from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class PlainSettings:
    model: str = "gpt-5.4"
    reasoning_effort: str = "high"
    personality: str = "none"
    web_search: str = "disabled"
    project_doc_max_bytes: int = 0
    history_persistence: str = "none"
    instructions: str = (
        "You are a plain content-generation assistant.\n"
        "Follow the user request directly.\n"
        "Do not load project-specific workflows unless the prompt explicitly asks for them.\n"
    )


def default_plain_settings() -> PlainSettings:
    return PlainSettings()
