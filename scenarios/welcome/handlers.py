from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from scenarios.welcome.text import START_TEXT

router = Router(name="welcome")

@router.message(CommandStart())
async def cmd_start(message: Message) -> None:
    await message.answer(START_TEXT)