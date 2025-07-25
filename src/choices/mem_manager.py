"""Memory manager choice module."""

from src import Choice
from src.memory_handler import MemoryHandler


class MemoryManager(Choice):

    """Memory manager choice class."""

    def __init__(self) -> None:
        """Constructor for the memory handler."""
        self.handler = MemoryHandler()

    def run(self) -> None:
        """Run the Memory manager."""
        print("\nClearing Memory...\n")
        self.handler.init_memory(force=True)
        print("\nMemory cleared successfully.\n")

