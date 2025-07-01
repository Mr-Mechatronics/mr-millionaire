"""Module to manage all the constant values used for this repository."""


class Breaks:

    """Line breaks & Spaces."""

    newline: str = "\n"
    space_2: str = "  "


class Numerics:

    """Numerical constant values used in this repository."""

    choice_range: tuple = (1, 4)
    max_attempt: int = 3


class LLMConst:

    """Open AI LLM constant values used in this repository."""

    api_key: str = "API_KEY"
    api_endpoint: str = "API_ENDPOINT"
    llm_model: str = "MODEL"
