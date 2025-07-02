"""Utility module for this repository."""
import sys

from src.lib_constant import Messages


def print_strikethrough(text: str, end: str = "\n") -> None:
    r"""Prints the given text with a strikethrough effect using ANSI escape codes.

    Args:
        text (str): The text to be printed.
        end (str, optional): The text to be printed. Defaults to "\n".

    """
    strikethrough_start = "\033[9m"
    reset_formatting = "\033[0m"

    print(f"{strikethrough_start}{text}{reset_formatting}", end=end)


def get_user_input(
        input_str: str,
        is_int: bool = False,
        constrains: list | tuple | None = None,
        max_attempt: int = 3,
        warning_msg: str | None = None,
        current_attempt: int = 1) -> int | str:
    """Get user input.

    Args:
        input_str (str): The text to be printed.
        is_int (bool, optional): Whether the input should be interpreted as an integer. Defaults to False.
        constrains (list | tuple, optional): A tuple of the possible constraints. Defaults to empty list.
        max_attempt (int, optional): The maximum number of attempts. Defaults to 3.
        warning_msg (str, optional): Warning message. Defaults to None.
        current_attempt (int, optional): Current attempt number. Defaults to 1.

    Returns:
        int | str: The user input.

    """
    if current_attempt > max_attempt:
        print(Messages.max_attempt_reached)
        sys.exit(1)
    if constrains is None:
        constrains = []
    user_input = input(input_str)
    if is_int:
        try:
            user_input = int(user_input)
        except ValueError:
            print(warning_msg if warning_msg
                  else Messages.default_int_err.format(attempts_left=max_attempt - current_attempt))
            current_attempt += 1
            return get_user_input(input_str, is_int, constrains, max_attempt, warning_msg, current_attempt)
    if constrains and user_input not in constrains:
        print(warning_msg if warning_msg
              else Messages.constrain_err.format(constrains=constrains, attempts_left=max_attempt - current_attempt))
        current_attempt += 1
        return get_user_input(input_str, is_int, constrains, max_attempt, warning_msg, current_attempt)
    return user_input
