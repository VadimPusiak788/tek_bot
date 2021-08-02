import re
from aiogram import types
from aiogram.dispatcher import handler
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler

from utils.db_api.models import User


class ACLMiddleware(BaseMiddleware):
    
    async def setup_chat(self, data: dict, user: types.User):
        
        user_id = user.id

        user = User.get_or_create(user_id)

        data['user'] = user


    async def on_pre_process_message(self, message: types.Message, data:dict): 
        await self.setup_chat(data, message.from_user)

    async def check_premisson(self, data: dict, message: types.Message):
        
        handler = current_handler.get()

        if not handler:
            return

        allow = getattr(handler, "allow", False)

        if allow:
            return 
        
        user = data.get('user')
        if not user.allowed:
            await message.reply("Доступ к боту запрещен")
            raise CancelHandler()
        
    async def on_process_message(self, message: types.Message, data: dict):
        await self.check_premisson(data, message)
