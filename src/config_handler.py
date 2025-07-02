"""Configuration handler module."""




class ConfigHandler:

    """Configuration handler class."""

    def __init__(self) -> None:
        """Configuration initializer."""
        self.config = self.read_current_config()

    @property
    def difficulty_level(self) -> int:
        """Return difficulty level.

        Returns:
            int: difficulty level

        """
        return self.config.get("difficulty_level")

    def read_current_config(self) -> None:
        """Reads current configuration from file and returns it."""
