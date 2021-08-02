import asyncio
from typing import Union

from aiogram import types
from aiogram.dispatcher.dispatcher import DEFAULT_RATE_LIMIT, Dispatcher
from aiogram.dispatcher.middlewares import BaseMiddleware
from aiogram.dispatcher.handler import CancelHandler, current_handler
from aiogram.types.callback_query import CallbackQuery
from aiogram.utils.exceptions import Throttled


class Troh(BaseMiddleware):
    
    def __init__(self, limit=DEFAULT_RATE_LIMIT, key_prefix='antiflood_'):
        self.limit = limit
        self.key_prefix = key_prefix
        super(Troh, self).__init__()
    
    async def throttle(self, target: Union[types.Message, types.CallbackQuery]):
        handler = current_handler.get()

        if not handler:
            return 

        dp = Dispatcher.get_current()
        limit = getattr(handler, 'throttling_rate_limit', self.limit)
        key = getattr(handler, 'throttling_key', f'{self.key_prefix}_{handler.__name__}')
        try:
            await dp.throttle(key, rate=limit)
        except Throttled as t:
            await self.target_throttle(target, t, dp, key)
            raise CancelHandler()

    async def target_throttle(self, target: Union[types.Message, types.CallbackQuery],
                            throttled: Throttled, dispatcher: Dispatcher, key: str):

        msg = target.message if isinstance(target, types.CallbackQuery) else target
        
        delta = throttled.rate - throttled.delta
        if throttled.exceeded_count == 2:
            await msg.reply("Часто")
            return
        
        elif throttled.exceeded_count == 3:
            await msg.reply(f'dont answer {delta}')
        
        await asyncio.sleep(delta)

        thr = await dispatcher.check_key(key)
        if thr.exceeded_count == throttled.exceeded_count:
            await msg.reply('All')
    
    async def on_process_message(self, message, data):
        await self.throttle(message)