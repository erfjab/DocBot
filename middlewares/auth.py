from typing import Any, Awaitable, Callable, Dict
from aiogram import BaseMiddleware
from aiogram.types import Update
from utils.log import logger
from db import crud

class CheckUser(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[Update, Dict[str, Any]], Awaitable[Any]],
        event: Update,
        data: Dict[str, Any]
    ) -> Any:
        user = None

        if event.message:
            user = event.message.from_user
        elif event.callback_query:
            user = event.callback_query.from_user
        elif event.inline_query:
            user = event.inline_query.from_user
        
        if not user:
            logger.warning('Received update without user information!')
            return None

        await crud.upsert_user(
            chatid=user.id,
            username=user.username
        )

        return await handler(event, data)