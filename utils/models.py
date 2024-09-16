from aiogram.filters.callback_data import CallbackData
from enum import Enum

class AdminPanelStatus(str, Enum):
    Home = 'home'
    Documents = 'documents'
    Users = 'users'

class AdminPanel(CallbackData, prefix='admin_panel'):
    page: AdminPanelStatus