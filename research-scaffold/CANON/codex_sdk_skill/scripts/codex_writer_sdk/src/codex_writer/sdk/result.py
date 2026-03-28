from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class GenerationOutput:
    text: str
    tokens_used: int = 0
