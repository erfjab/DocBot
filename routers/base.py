from aiogram import Router, F
from aiogram.filters.command import CommandStart, Command
from aiogram.types import Message

from utils.lang import MessageText

router = Router()

@router.message(CommandStart(ignore_case=True))
async def start(message: Message):

    return await message.answer(
        text=MessageText.Start,
        reply_markup=...
    )