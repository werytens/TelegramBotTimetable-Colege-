from aiogram import types
from main import dp
import json
import datetime
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

    await message.answer(f"<u><b>Привет! Команды бота TBTC:</b></u>\n\n/help - эта команда.\n/lesson - узнать информацию о паре, которая идёт сейчас.\n/timetable - узнать общее расписание.\n/weekinfo - информация о текущей неделе.\n\n<u><b>В разработке:</b></u>\n\n1. Функционал, позволяющий записывать и получить домашнее задание в соответствии с расписанием.\n2. Функционал, позволяющий узнать замены.\n\n<u><b>Информация о боте:</b></u>\n\n<b>Версия бота: </b>1.0.3.\n~ Stable V1", reply_markup = greet_kb, parse_mode = "HTML")
             

@dp.message_handler(commands = ["weekinfo"])
async def weekinfocommand(message: types.Message):
    with open("jsons/main.json", "r") as f:
        table = json.load(f)

    firstWeekMonday = table["firstWeekMonday"]
    firstWeekMonday = datetime.datetime.strptime(firstWeekMonday, '%d-%m-%Y')
    days = (datetime.datetime.now() - firstWeekMonday).days

    perm = days // 7 / 2

    if perm == 0:
        table["key"] = 2
    elif perm != 0:
        table["key"] = 1
    

    if table["key"] == 1:
        weekStatus = 'Числитель'
    else:
        weekStatus = "Знаменатель"
    
    await message.answer(f"<u><b>Информация о текущей неделе:</b></u>\n\n<b>Эта неделя: </b>{weekStatus}.", parse_mode = "HTML")


    with open("jsons/main.json", "w", encoding = "UTF-8") as file:
        json.dump(table, file)

@dp.message_handler()
async def othermessage(message: types.Message):
    with open("jsons/main.json", "r") as f:
        table = json.load(f)

    firstWeekMonday = table["firstWeekMonday"]
    firstWeekMonday = datetime.datetime.strptime(firstWeekMonday, '%d-%m-%Y')
    days = (datetime.datetime.now() - firstWeekMonday).days

    perm = days // 7 / 2

    if perm == 0:
        table["key"] = 2
    elif perm != 0:
        table["key"] = 1
    
    await message.answer('Команда не распознана')

    with open("jsons/main.json", "w", encoding = "UTF-8") as file:
        json.dump(table, file)