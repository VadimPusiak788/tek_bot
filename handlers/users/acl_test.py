from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from utils.db_api.models import User
from utils.misc.allowed import allow_access


@allow_access()
@dp.message_handler(Command('block_me'))
async def block_me(message: types.Message, user:User):
    user.block()

    await message.answer(f"Allowed user {user.allowed}")


@allow_access()
@dp.message_handler(Command('unblock_me'))
async def block_me(message: types.Message, user:User):
    user.unblock()

    await message.answer(f"Unblock user {user.allowed}")

