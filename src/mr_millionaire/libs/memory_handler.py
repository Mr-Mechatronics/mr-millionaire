"""Memory DB handler."""

from mr_millionaire.libs.lib_constant import Breaks, ConfigVal


class MemoryHandler:

    """Memory DB handler."""

    def __init__(self) -> None:
        """Constructor for Memory handler."""
        self.found_in_memory = []

    def init_memory(self, force: bool = False) -> list:
        """Initialize the memory file.

        Args:
            force (bool): Flag to clear and initialize the memory again.

        Returns:
            list: List of questions in memory.

        """
        if ConfigVal.memory.exists() and not force:
            with ConfigVal.memory.open("r") as memory:
                return [q.strip() for q in memory.readlines()]
        with ConfigVal.memory.open("w") as memory:
            return []

    def add_to_memory(self, question: str) -> None:
        """Add the question to memory file.

        Args:
            question (str): Question to be added to memory.

        """
        with ConfigVal.memory.open("a") as memory:
            memory.write(question + Breaks.newline)

    def already_seen(self, question: str) -> bool:
        """Check if the question is already seen.

        Args:
            question (str): Question to be checked whether it is already there in memory.

        Returns:
            bool: True if the question found else False.

        """
        return question in self.init_memory()
