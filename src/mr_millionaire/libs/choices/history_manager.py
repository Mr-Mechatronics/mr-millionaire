"""History manager choice module."""

from datetime import datetime

from tabulate import tabulate

from mr_millionaire.libs import Choice
from mr_millionaire.libs.lib_constant import ConfigVal


class HistoryManager(Choice):

    """History manager choice class."""

    def run(self) -> None:
        """Run the History manager."""
        if ConfigVal.history_location.exists():
            with ConfigVal.history_location.open("r") as history:
                details = history.readlines()
                self._show_history(details)
        else:
            print("No Records found")

    @staticmethod
    def write_to_history(player_name: str, prize_won: int) -> None:
        """Write last player record to history.

        Args:
            player_name (str): Name of the player.
            prize_won (int): Prize money won.

        """
        date_time = datetime.now().strftime(ConfigVal.datetime_format)
        content = f"{date_time},{player_name},$ {prize_won}\n"
        mode = "w" if not ConfigVal.history_location.exists() else "a"
        with ConfigVal.history_location.open(mode) as history_f:
            history_f.write(content)


    @staticmethod
    def _show_history(details: list) -> None:
        """Shows the past history.

        Args:
            details (list): List of lines read from history file.

        """
        data = [entry.strip().split(",") for entry in details]
        print(tabulate(data, headers=ConfigVal.history_headers, tablefmt="grid"))
