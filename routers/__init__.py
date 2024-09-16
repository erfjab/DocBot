
from aiogram import Router

def setup_routers() -> Router:
    from . import (
        base,
    )
    router = Router()

    router.include_router(base.router)
    return router
