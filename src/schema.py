"""Quiz question schema."""


from pydantic import BaseModel, Field, ValidationInfo, conlist, field_validator


class FiftyFiftyAnswer(BaseModel):

    """Answer choices for the question."""

    choices: conlist(str, min_length=2, max_length=2) = Field(
        ..., description="Exactly two choices in which 1 is a correct answer.",
    )
    correct_answer: str = Field(
        ..., description="Correct answer (must match one of the choices).",
    )

    @field_validator("correct_answer")
    @classmethod
    def answer_must_be_in_choices(cls, v: str, info: ValidationInfo) -> str:
        """Field validator to verify the correct answer in choices."""
        if v not in info.data.get("choices", []):
            msg = "correct_answer must be one of the choices"
            raise ValueError(msg)
        return v


class PhoneFriendAnswer(BaseModel):

    """Answer to the phone friend question."""

    answer: str = Field(
        ..., description="Correct answer to the question.",
    )

class QuestionSchema(BaseModel):

    """A single multiple‑choice question with exactly four options."""

    question: str = Field(
        ..., description="Question shown to the player.",
    )
    choices: conlist(str, min_length=4, max_length=4) = Field(
        ..., description="Exactly four answer choices.",
    )
    correct_answer: str = Field(
        ..., description="Correct answer (must match one of the choices).",
    )


    @field_validator("correct_answer")
    @classmethod
    def answer_must_be_in_choices(cls, v: str, info: ValidationInfo) -> str:
        """Field validator to verify the correct answer in choices."""
        if v not in info.data.get("choices", []):
            msg = "correct_answer must be one of the choices"
            raise ValueError(msg)
        return v


class PlayerName(BaseModel):

    """Player name schema."""

    name: str = Field(
        ..., description="Name of the scientist.",
    )
