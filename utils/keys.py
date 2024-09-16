from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from utils.lang import KeyboardText
from utils.models import AdminPanel, AdminPanelStatus

def start(link: str) -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=KeyboardText.Link, 
                web_app=WebAppInfo(url=link)
            ),
        ]
    ])

def admin() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(
                text=KeyboardText.Servers, 
                callback_data=AdminPanel(page=AdminPanelStatus.Servers).pack()
            ),
        ]
    ])