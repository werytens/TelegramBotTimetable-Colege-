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
    weekinfo = KeyboardButton('/weekinfo')
    eventsinfo = KeyboardButton('/eventsinfo')
    

    greet_kb = ReplyKeyboardMarkup()
    greet_kb.add(button_help)
    greet_kb.add(button_lesson)
    greet_kb.add(button_timetable)
    greet_kb.add(weekinfo, eventsinfo)

    await message.answer(f"<u><b>Привет! Команды бота TBTC:</b></u>\n\n/help - эта команда.\n/lesson - узнать информацию о паре, которая идёт сейчас.\n/timetable - узнать общее расписание.\n/weekinfo - информация о текущей неделе.\n/eventsinfo - узнать информацию о событиях.\n\n<u><b>Информация о боте:</b></u>\n\n<b>Версия бота: </b>2.2.0.\n<b>ЯП: </b>Python.\n<b>Библиотека: </b>Aiogram.\n~ Stable V1", reply_markup = greet_kb, parse_mode = "HTML")
             

@dp.message_handler(commands = ["weekinfo"])
async def weekinfocommand(message: types.Message):
    with open("jsons/main.json", "r") as f:
        table = json.load(f)

    firstWeekMonday = datetime.datetime.strptime("30-01-2023", '%d-%m-%Y')
    days = (datetime.datetime.now() - firstWeekMonday).days

    if days // 7 % 2 == 0:
        table["key"] = 2
    else:
        table["key"] = 1
    

    if table["key"] == 2:
        weekStatus = 'Числитель'
    else:
        weekStatus = "Знаменатель"
    
    await message.answer(f"<u><b>Информация о текущей неделе:</b></u>\n\n<b>Эта неделя: </b>{weekStatus}.", parse_mode = "HTML")

    with open("jsons/main.json", "w", encoding = "UTF-8") as file:
        json.dump(table, file)

@dp.message_handler(commands = ["eventsinfo"])
async def eventsinfo(message: types.Message):
    th = (datetime.datetime.strptime("8-03-2023", '%d-%m-%Y') - datetime.datetime.now()).days
    tt = (datetime.datetime.strptime("8-02-2023", '%d-%m-%Y') - datetime.datetime.now()).seconds

    def toFixed(numObj, digits = 0):
        return f"{numObj:.{digits}f}"
    
    def knowDateFor(_date):
        th = (datetime.datetime.strptime(_date, '%d-%m-%Y') - datetime.datetime.now()).days
        tt = (datetime.datetime.strptime(_date, '%d-%m-%Y') - datetime.datetime.now()).seconds

        hours = int(toFixed(((tt / 3600) + (th * 24))))

        if hours >= 24: date = f"{toFixed(hours / 24)} дней"
        else: date = f"{hours} час(а/ов)"

        return date
        
    date8mart = knowDateFor("8-03-2023")
    datefinally = knowDateFor("1-07-2023")
    

    await message.answer(f"<u><b>Информация о различных событиях:</b></u>\n\n<b>Времени до 8-го марта: </b>{date8mart}.\n<b>Времени до конца года: </b>{datefinally}.", parse_mode = "HTML")

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