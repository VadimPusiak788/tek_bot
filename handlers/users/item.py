from aiogram.dispatcher.filters import Command
from aiogram import types

from loader import dp
from keyboards.inline.choice_button import choice, pear_keyboard

@dp.message_handler(Command('items'))
async def show_items(message: types.Message):
    await message.answer(text="have items", reply_markup=choice)


@dp.callback_query_handler(text_contains='pear')
async def buy_pear(call: types.CallbackQuery):
    await call.answer(cache_time=60)

    callback_data = call.data
    print(callback_data)
    
    await call.message.answer('Pear', reply_markup=pear_keyboard)