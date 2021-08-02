from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types.user import User

from loader import dp
from utils.misc import rate_limit


@rate_limit(5, key='start')
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message, user: User):
    await message.answer(f"Привет, {message.from_user.full_name}!")
