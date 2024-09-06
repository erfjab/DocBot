from decouple import config

# Function to check if a required configuration value is missing
def require_setting(setting_name, value):
    if not value:
        raise ValueError(f"The '{setting_name}' setting is required and cannot be empty.")

# Telegram Bot Settings
BOT_TOKEN = config('BOT_TOKEN', cast=str)  # required
require_setting('BOT_TOKEN', BOT_TOKEN)

ADMINS_CHATID = config(
    'ADMINS_CHATID',
    default='',
    cast=lambda v: [int(i) for i in filter(str.isdigit, (s.strip() for s in v.split(',')))]
)  # required

BOT_NAME = config('BOT_NAME', default='MarzDoc', cast=str)
