from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from keyboards.default import menu


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Show menu', reply_markup=menu)