from aiogram import types
from main import dp
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton
 
@dp.message_handler(commands = ['start', 'help'])
async def send_welcome(message: types.Message):
    button_help = KeyboardButton('/help')
    button_lesson = KeyboardButton('/lesson')
    button_timetable = KeyboardButton('/timetable')

    greet_kb = ReplyKeyboardMarkup()
    greet_kb.add(button_help)
    greet_kb.add(button_lesson)
    greet_kb.add(button_timetable)

    await message.answer(f"<u><b>Привет! Команды бота TBTC:</b></u>\n\n/help - эта команда.\n/lesson - узнать информацию о паре, которая идёт сейчас.\n/timetable - узнать общее расписание.\n\n<u><b>В разработке:</b></u>\n\n1. Функционал, позволяющий записывать и получить домашнее задание в соответствии с расписанием.", reply_markup = greet_kb, parse_mode = "HTML")
             

@dp.message_handler()
async def othermessage(message: types.Message):

    await message.answer('Команда не распознана.')
