"""Main module to run the game."""

import sys

from dotenv import load_dotenv

from src.choices import ConfigManager, GameRunner, MemoryManager
from src.lib_constant import Breaks, Numerics

load_dotenv()


def ask_choice(attempt: int = 1) -> int:
    """User entry for the game.

    Args:
        attempt (int): Number of attempts made. Default is 1.

    Return:
        int: Index of the choice.

    """
    choice = int(input("Enter your choice: "))
    if attempt == Numerics.max_attempt:
        print("Max attempt reached. You must be 'Blind' or 'illiterate'.")
        sys.exit(1)
    if choice not in range(*Numerics.choice_range):
        attempt += 1
        return ask_choice(attempt)
    return choice

def choose_choice() -> int:
    """Header function to display available choices."""
    print(f"Choose one from options:{Breaks.newline}"
          f"{Breaks.space_2}[1] Play Game{Breaks.newline}"
          f"{Breaks.space_2}[2] Clear Memory{Breaks.newline}"
          f"{Breaks.space_2}[3] Configuration{Breaks.newline}")
    return ask_choice()

def process_choice(choice: int) -> None:
    """Process the user choice.

    Args:
        choice (int): Index of the choice.

    """
    choice_processing = {
        1 : GameRunner(),
        2 : MemoryManager(),
        3 : ConfigManager(),
    }
    process = choice_processing.get(choice)
    process.run()

def start_game() -> None:
    """Main function that starts the game."""
    print(f"Welcome to MillionAIRE!{Breaks.newline}")
    choice = choose_choice()
    process_choice(choice)


if __name__ == "__main__":
    start_game()
