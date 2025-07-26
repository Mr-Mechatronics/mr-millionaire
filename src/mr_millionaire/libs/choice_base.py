"""Game choice's Abstract."""

from abc import ABC, abstractmethod


class Choice(ABC):

    """Abstract class of choice."""

    @abstractmethod
    def run(self) -> None:
        """Run method to run the choice."""
