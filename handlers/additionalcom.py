from aiogram import types
from main import dp, Bot
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

from aiogram.dispatcher.filters import Text
from aiogram.utils import executor

bot = Bot

keyboard = InlineKeyboardMarkup()
day_1 = InlineKeyboardButton(text='Понедельник', callback_data="day_1")
day_2 = InlineKeyboardButton(text='Вторник', callback_data="day_2")
day_3 = InlineKeyboardButton(text='Среда', callback_data="day_3")
day_4 = InlineKeyboardButton(text='Четверг', callback_data="day_4")
day_5 = InlineKeyboardButton(text='Пятница', callback_data="day_5")
keyboard.add(day_1, day_2, day_3)
keyboard.add(day_4, day_5)



@dp.message_handler(commands = ['timetable'])
async def timetable(message: types.Message):
    await message.answer("""
    <u><b>Расписание: </b></u>\n\n<b>— Понедельник</b>\n\n1. Технический иностранный | 46 кабинет.\n2. Поддержка и тестирование программных модулей | 40 кабинет.\n3. Разработка программных решений (Blockchain) | 43 кабинет.\n4. Иностранный язык | 45/46 кабинеты.

<b>— Вторник</b>\n
1. Объектно-ориентировочный язык программирования JavaScript | 43 кабинет.
2. Объектно-ориентировочный язык программирования JavaScript | 43 кабинет.
3. Основы алгоритмизации и программирования | 26 кабинет.
4. Архитектура аппаратных средств | 34 кабинет.

<b>— Среда</b>\n
1. Ничего.
2. Основы алгоритмизации и программирования | 26 кабинет.
3. Физическая культура.
4. Безопасность жизнедеятельности | 35 кабинет.

<b>— Четверг</b>\n
1. Технология разработки и защиты баз данных | 43 кабинет.
2. Теория вероятности и математическая статистика | 30 кабинет.
3. Технология разработки и защиты баз данных. / Объектно-ориентировочный язык программирования JavaScript | 43 кабинет.
4. Поддержка и тестирование программных модулей | 37 кабинет.

<b>— Пятница</b>\n
1. Архитектура аппаратных средств | 34 кабинет.
2. Компьютерные сети | 39 кабинет.
3. Элементы высшей математики | 44 кабинет.
4. Безопасность жизнедеятельности | 35 кабинет. / Поддержка и тестирование программных модулей | 37 кабинет.""", reply_markup=keyboard , parse_mode = "HTML")


@dp.callback_query_handler(text_contains='day_')
async def menu(call: types.CallbackQuery):
    if call.data and call.data.startswith("day_"):
        code = call.data[-1:]
        if code.isdigit():
            code = int(code)
        if code == 1:
            await call.message.edit_text('Расписание в понедельник:\n\n1. Технический иностранный | 46 кабинет.\n2. Поддержка и тестирование программных модулей | 40 кабинет.\n3. Разработка программных решений (Blockchain) | 43 кабинет.\n4. Иностранный язык | 45/46 кабинеты.', reply_markup=keyboard)
        if code == 2:
            await call.message.edit_text('Расписание во вторник:\n\n1. Объектно-ориентировочный язык программирования JavaScript | 43 кабинет.\n2. Объектно-ориентировочный язык программирования JavaScript | 43 кабинет.\n3. Основы алгоритмизации и программирования | 26 кабинет.\n4. Архитектура аппаратных средств | 34 кабинет.', reply_markup=keyboard)
        if code == 3:
            await call.message.edit_text('Расписание в среду:\n\n1. Ничего.\n2. Основы алгоритмизации и программирования | 26 кабинет.\n3. Физическая культура.\n4. Безопасность жизнедеятельности | 35 кабинет.', reply_markup=keyboard)
        if code == 4:
            await call.message.edit_text('Расписание в четверг:\n\n1. Технология разработки и защиты баз данных | 43 кабинет.\n2. Теория вероятности и математическая статистика | 30 кабинет.\n3. Технология разработки и защиты баз данных. / Объектно-ориентировочный язык программирования JavaScript | 43 кабинет.\n4. Поддержка и тестирование программных модулей | 37 кабинет.', reply_markup=keyboard)
        if code == 5:
            await call.message.edit_text('Расписание в пятницу:\n\n1. Архитектура аппаратных средств | 34 кабинет.\n2. Компьютерные сети | 39 кабинет.\n3. Элементы высшей математики | 44 кабинет.\n4. Безопасность жизнедеятельности | 35 кабинет. / Поддержка и тестирование программных модулей | 37 кабинет.', reply_markup=keyboard)
        else:
            await bot.answer_callback_query(call.id)
