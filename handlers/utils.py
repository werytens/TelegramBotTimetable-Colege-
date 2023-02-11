from aiogram import types
from main import dp
 
@dp.message_handler(commands = ['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer(f"<u><b>Привет! Команды бота TBTC:</b></u>\n\n/help - эта команда.\n/lesson - узнать информацию о паре, которая идёт сейчас.\n/timetable - узнать общее расписание.\n\n<u><b>В разработке:</b></u>\n\n1. Функционал, позволяющий записывать и получить домашнее задание в соответствии с расписанием.", parse_mode = "HTML")
            

@dp.message_handler()
async def othermessage(message: types.Message):

    await message.answer('Команда не распознана.')
