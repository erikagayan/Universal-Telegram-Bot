import asyncio

from aiogram import Bot, Dispatcher

from config import settings
from scenarios.welcome import router as welcome_router

dp = Dispatcher()
dp.include_router(welcome_router)


async def main() -> None:
    bot = Bot(token=settings.bot_token.get_secret_value())
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())