from aiogram import types


from loader import dp
from filters import IsGroup


@dp.message_handler(IsGroup(), content_types=types.ContentType.NEW_CHAT_MEMBERS)
async def new_member(messange: types.Message):
    member = ', '.join([m.first_name for m in messange.new_chat_members])
    await messange.reply(f'Hello, {member}')