from aiogram import Dispatcher

from loader import dp
from .throttling import Troh
from .acl import ACLMiddleware

if __name__ == "middlewares":
    dp.middleware.setup(Troh())
    dp.middleware.setup(ACLMiddleware())
