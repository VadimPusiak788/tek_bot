from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from keyboards.inline.callback_datas import buy_callback


choice = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Apple', callback_data='buy:apple'),
            InlineKeyboardButton(text='Pie', callback_data=buy_callback.new(item_name='pear', quantity=2))
        ],
        [
            InlineKeyboardButton(text='Cancel', callback_data='cancel')
        ]
    ]
)

pear_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
        InlineKeyboardButton(text='Pear here', url='https://telegra.ph/Ispolzovanie-Middlwares-v-aiogram-08-14')
        ]
    ]
)