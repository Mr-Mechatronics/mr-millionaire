"""Configuration handler module."""
import json

from src.lib_constant import Breaks, ConfigVal, Messages
from src.utility import DotDict


class ConfigHandler:

    """Configuration handler class."""

    @property
    def configuration(self) -> dict:
        """Returns the current configuration as property.

        Returns:
            dict: Current configuration dictionary.

        """
        return DotDict(self.init_config())

    def init_config(self) -> dict:
        """Initialize configuration.

        Returns:
            dict: Initialized configuration dictionary.

        """
        if ConfigVal.config_path.exists():
            with ConfigVal.config_path.open("r") as f:
                return json.load(f)
        return {}

    def set_llm_config(self) -> None:
        """Set LLM related environmental var as configuration."""
        print(Messages.llm_config_msg)

        env_var_name = input("LLM Environment Variable Name : ")
        env_var_value = input("LLM Environment Variable Value : ")
        model_name = input("LLM Model (eg: groq/gemma2-9b-it) : ")

        env_content = f"{env_var_name.upper()}={env_var_value}\nMODEL={model_name}"

        with ConfigVal.env_path.open("w") as env_file:
            env_file.write(env_content)

        print(f"{Breaks.newline}Environment config files are saved to '{ConfigVal.env_path}' location.{Breaks.newline}")

    def set_configuration(self) -> None:
        """Set game configuration."""
        current_config = self.init_config()
        print(Messages.settings_header)
        configuration = current_config if current_config else ConfigVal.default_configuration
        new_configuration = {}

        for config_key, config_value in configuration.items():
            user_input = input(f"Configuration - {config_key} | Current - {config_value} | To Change : ")
            new_configuration[config_key] = user_input if user_input else config_value

        self._write_configuration(new_configuration)


    def set_initial_configuration(self) -> None:
        """Set required initial configuration on game run."""
        if not ConfigVal.core_path.exists():
            ConfigVal.core_path.mkdir(parents=True)

        if not ConfigVal.env_path.exists():
            self.set_llm_config()

        if not ConfigVal.config_path.exists():
            self.set_configuration()

    @staticmethod
    def _write_configuration(configuration: dict) -> None:
        """Write the game configuration to config file.

        Args:
            configuration (dict): Configuration dictionary.

        """
        with ConfigVal.config_path.open("w") as f:
            json.dump(configuration, f, indent=4)



