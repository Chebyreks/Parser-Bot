import asyncio

from aiogram import Bot, Dispatcher

from parser_bot.core.config import settings
from parser_bot.core.db import AsyncSessionLocal
from parser_bot.core.db_middleware import DatabaseMiddleware
from parser_bot.handlers.commands_router import router as commands_router


async def main():
    bot = Bot(token=settings.telegram_bot_token)
    dp = Dispatcher()

    dp.update.middleware(DatabaseMiddleware(session_pool=AsyncSessionLocal))
    dp.include_routers(commands_router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())