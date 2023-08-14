from dataclasses import dataclass


@dataclass
class LLMResponse:
    text: str
    finish_reason: str
    total_tokens: int = 0
