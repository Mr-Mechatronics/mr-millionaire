"""Game runner choice module."""


from dataclasses import dataclass

from src import Choice
from src.llm_handler import LLMHandler


@dataclass
class Question:

    """Question dataclass."""

    question_no: int
    question: str
    choices: list[str]
    correct_answer: str


class GameRunner(Choice):

    """Game runner choice class."""

    def __init__(self) -> None:
        """Constructor for GameRunner."""
        self.llm_handler = LLMHandler()
        self.prize_won = 0
        self._question_history = []
        self._question_no = 0


    def generate_next_question(self) -> Question:
        """Generate next question to be asked to the player.

        Returns:
            Question: next question to be asked to the player.

        """
        question_prompt = self._construct_question_prompt()
        question = Question(
            question_no=self._question_no + 1, **self.llm_handler.request_llm(question_prompt ),
        )
        self._question_history.append(question)
        return question

    @staticmethod
    def _construct_question_prompt() -> None:
        """Construct question prompt.

        Returns:
            str: Question prompt.

        """
