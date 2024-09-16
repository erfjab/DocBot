import json
from typing import Dict, Optional
from utils.log import logger

# Configuration file path
CONFIG_FILE = 'data/.info.json'

class ConfigManager:
    _config: Optional[Dict] = None

    @staticmethod
    def _load_config() -> Optional[Dict]:
        try:
            with open(CONFIG_FILE, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            logger.error(f"JSON file '{CONFIG_FILE}' does not exist!")
            return None
        except json.JSONDecodeError:
            logger.error("Error decoding JSON file!")
            return None

    @staticmethod
    def get_config() -> Optional[Dict]:
        if ConfigManager._config is None:
            ConfigManager._config = ConfigManager._load_config()
        return ConfigManager._config

    @staticmethod
    def get_bot_token() -> Optional[str]:
        config = ConfigManager.get_config()
        if config is None:
            return None
        return config.get('BOT_TOKEN', {})

    @staticmethod
    def get_bot_name() -> Optional[str]:
        config = ConfigManager.get_config()
        if config is None:
            return None
        return config.get('BOT_NAME', 'DocBot')

    @staticmethod
    def get_all_admin_keys() -> Optional[Dict[int, str]]:
        config = ConfigManager.get_config()
        if config is None:
            return None
        return config.get('ADMINS_CHATID', [])

    @staticmethod
    def is_admin(chat_id: int) -> bool:
        return chat_id in ConfigManager.get_all_admin_keys()

    @staticmethod
    def get_lang_key(key: str) -> Optional[str]:
        config = ConfigManager.get_config()
        if config is None:
            return None
        language: dict = config.get('LANGUAGE_SETTINGS', {})
        return language.get(key, {}) if language else {}
