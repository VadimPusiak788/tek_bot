from aiogram.types import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard import KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Cat")
        ],
        [
            KeyboardButton(text='Dog'),
            KeyboardButton(text='Pig')
        ],
    ],
    resize_keyboard=True
)