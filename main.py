"""Main module to run the game."""

from dotenv import load_dotenv

from src.choices import ConfigManager, GameRunner, MemoryManager
from src.lib_constant import Breaks
from src.utility import get_user_input

load_dotenv()


def choose_choice() -> int:
    """Header function to display available choices."""
    print(f"Choose one from options:{Breaks.newline}"
          f"{Breaks.space_2}[1] Play Game{Breaks.newline}"
          f"{Breaks.space_2}[2] Clear Memory{Breaks.newline}"
          f"{Breaks.space_2}[3] Configuration{Breaks.newline}")
    return get_user_input(
        "Enter your choice: ",
        is_int=True,
        constrains=list(range(1, 4)),
    )

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
