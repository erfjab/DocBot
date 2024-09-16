from enum import Enum
from utils.config import ConfigManager

class MessageText(str, Enum):
    Start = 'Start'
    Help = 'Help'
    
    def __str__(self) -> str:
        """Return the language value or default when accessing the enum."""
        return self._get_value()
    
    def _get_value(self) -> str:
        """Retrieve the corresponding value from config or return default."""
        config_value = ConfigManager.get_lang_key(self.value)
        if config_value:
            return config_value
        return self._get_default()

    def _get_default(self) -> str:
        """Return the default text for each message key."""
        defaults = {
            MessageText.Start: 'Welcome to DocBot',
            MessageText.Help: 'For use this bot, type @botusername to any chat',
        }
        return defaults.get(self, f'Unknown key: {self.value}')

class KeyboardText(str, Enum):
    Documents = 'Docs'
    Users = 'Users'
    Link = 'Link'

    def __str__(self) -> str:
        """Return the language value or default when accessing the enum."""
        return self._get_value()
    
    def _get_value(self) -> str:
        """Retrieve the corresponding value from config or return default."""
        config_value = ConfigManager.get_lang_key(self.value)
        if config_value:
            return config_value
        return self._get_default()

    def _get_default(self) -> str:
        """Return the default text for each message key."""
        defaults = {
            KeyboardText.Documents: 'docs',
            KeyboardText.Users: 'users',
        }
        return defaults.get(self, f'Unknown key: {self.value}')