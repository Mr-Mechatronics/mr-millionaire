"""Configuration manager choice module."""

from mr_millionaire.libs import Choice
from mr_millionaire.libs.config_handler import ConfigHandler
from mr_millionaire.libs.utility import get_user_input


class ConfigManager(Choice):

    """Configuration manager choice class."""

    def __init__(self) -> None:
        """Constructor for Configuration Manager."""
        self.handler = ConfigHandler()

    def run(self) -> None:
        """Run the configuration manager."""
        print("\nConfiguration Manager:\n")
        print("[1] LLM Configuration\t\t[2] Game Configuration")

        user_choice = get_user_input("\nChoice : ", is_int=True, constrains=range(1,2))
        if user_choice == 1:
            self.handler.set_llm_config()
        else:
            self.handler.set_configuration()
