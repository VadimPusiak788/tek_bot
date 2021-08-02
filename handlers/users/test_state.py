from aiogram.dispatcher.filters import Command, state
from aiogram import types
from aiogram.dispatcher import FSMContext


from loader import dp
from states.test import Test

@dp.message_handler(Command('test'), state=None)
async def enter_test(message: types.Message):
    await message.answer('Start test')
    await Test.Q1.set()


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    await message.answer('Test 2')
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(message: types.Message ,state: FSMContext ):
    await state.update_data(answer2=message.text)
    data = await state.get_data()
    await message.answer(data)

    await state.finish()
