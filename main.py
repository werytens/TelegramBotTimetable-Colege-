from aiogram import Bot, Dispatcher, executor, types
import calendar
import json
import datetime

#
#
#

# Для добавления хендлера нужно добавить новый файл в папку handlers, после чего в __init__.py записать "from .filename import dp". Внутри нового хендлера прописать следующие строки:
# from aiogram import types
# from main import dp

timetable = {
    1: {
        1: "8:50:00 - 10:20:00 | Технический иностранный.",
        2.1: "10:40:00 - 11:25:00 | Поддержка и тестирование программных модулей.",
        2.2: "11:45:00 - 12:30:00 | Поддержка и тестирование программных модулей.",
        3: "12:40:00 - 14:10:00 | Разработка программных решений (Blockchain).",
        4: "14:20:00 - 15:50:00 | Иностранный язык.",
    }, 
    2: {
        1: "8:00:00 - 9:30:00 | Объектно-ориентировочный язык программирования JavaScript.",
        2.1: "9:40:00 - 10:25:00 | Объектно-ориентировочный язык программирования JavaScript.",
        2.2: "10:45:00 - 11:30:00 | Объектно-ориентировочный язык программирования JavaScript.",
        3: "11:50:00 - 13:20:00 | Основы алгоритмизации и программирования.",
        4: "13:30:00 - 15:00:00 | Архитектура аппаратных средств."
    }, 
    3: {
        1: "8:00:00 - 9:30:00 | Пара отдыха (дома).",
        2.1: "9:40:00 - 10:25:00 | Основы алгоритмизации и программирования.",
        2.2: "10:45:00 - 11:30:00 | Основы алгоритмизации и программирования.",
        3: "11:50:00 - 13:20:00 | Физическая культура.",
        4: "13:30:00 - 15:00:00 | Безопасность жизнедеятельности."
    }, 
    4: {
        1: "8:00:00 - 9:30:00 | Технология разработки и защиты баз данных.",
        2.1: "9:40:00 - 10:25:00 | Теория вероятности и математическая статистика.",
        2.2: "10:45:00 - 11:30:00 | Теория вероятности и математическая статистика.",
        3: "11:50:00 - 13:20:00 | Технология разработки и защиты баз данных. / Объектно-ориентировочный язык программирования JavaScript.",
        4: "13:30:00 - 15:00:00 | Поддержка и тестирование программных модулей."
    },
    5: {
        1: "8:00:00 - 9:30:00 | Архитектура аппаратных средств.",
        2.1: "9:40:00 - 10:25:00 | Компьютерные сети.",
        2.2: "10:45:00 - 11:30:00 | Компьютерные сети.",
        3: "11:50:00 - 13:20:00 | Элементы высшей математики.",
        4: "13:30:00 - 15:00:00 | Безопасность жизнедеятельности. / Поддержка и тестирование программных модулей."
    }
}

with open("token.json", "r") as file:
    tokenfile = json.load(file)

TOKEN = tokenfile["token"]

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands = ['lesson'])
async def send_welcome(message: types.Message):
    def TimeCalc(end, now):
        return (str(end - now)[-7:-3])


    timeNow = datetime.datetime.now()
    day = datetime.datetime.isoweekday(datetime.datetime.now())
    # timeNow = datetime.datetime.strptime('10-02-2023 10:20:00', '%d-%m-%Y %H:%M:%S'); day = 5

    if day == 1:
        if datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str(timetable[1][1][:7]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[1][1][10:18]), '%H:%M:%S'):
            endTime = datetime.datetime.strptime(str(timetable[1][1][10:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №1</b>.\n<b>Название:</b> {(str(timetable[day][1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.1]))[22:]}", parse_mode = "HTML")

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str(timetable[1][2.1][:8]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[1][2.1][11:18]), '%H:%M:%S'):
            endTime = datetime.datetime.strptime(str(timetable[1][2.1][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.1]))[22:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.1]))[22:]}", parse_mode = "HTML")
            
        
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str(timetable[1][2.2][:8]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[1][2.2][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.2]))[22:]}, пара номер 2, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[1][2.2][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.2]))[22:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][3]))[22:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str(timetable[1][3][:8]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[1][3][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][3]))[22:]}, пара номер 3, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[1][3][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №3</b>.\n<b>Название:</b> {(str(timetable[day][3]))[22:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][4]))[22:]}", parse_mode = "HTML")

        
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str(timetable[1][4][:8]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[1][4][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][4]))[22:]}, пара номер 4, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[1][4][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №4</b>.\n<b>Название:</b> {(str(timetable[day][4]))[22:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.", parse_mode = "HTML")
            
        
        else: 
            await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число. Время: {str(timeNow)[11:19]}.\n\n\n\n{timeNow}')
    
    elif day == 2:
        if datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str(timetable[2][1][:7]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[2][1][10:17]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][1]))[20:]}, пара номер 1, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[2][1][10:17]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №1</b>.\n<b>Название:</b> {(str(timetable[day][1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.1]))[20:]}", parse_mode = "HTML")
            
        
        elif datetime.datetime.strptime((str(timeNow)[11:19]), '%H:%M:%S') >= datetime.datetime.strptime(str(timetable[2][2.1][:7]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[2][2.1][10:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.1]))[20:]}, пара номер 2, до конца пары .')

            endTime = datetime.datetime.strptime(str(timetable[2][2.1][10:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.2]))[20:]}", parse_mode = "HTML")
            
        
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[2][2.2][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[2][2.2][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.2]))[20:]}, пара номер 2, до конца пары .')

            endTime = datetime.datetime.strptime(str(timetable[2][2.2][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.2]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][3]))[20:]}", parse_mode = "HTML")
            
       
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[2][3][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[2][3][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][3]))[20:]}, пара номер 3, до конца пары .')

            endTime = datetime.datetime.strptime(str(timetable[2][3][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №3</b>.\n<b>Название:</b> {(str(timetable[day][3]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][4]))[20:]}", parse_mode = "HTML")
            
        
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[2][4][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[2][4][11:18]), '%H:%M:%S'):
            # await message.answer(f'Сейчас пара: {(str(timetable[day][4]))[20:]}, пара номер 4, до конца пары .')

            endTime = datetime.datetime.strptime(str(timetable[2][4][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №4</b>.\n<b>Название:</b> {(str(timetable[day][4]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.", parse_mode = "HTML")
            
    
        else: 
            await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')
    
    elif day == 3:
        if datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[3][1][:7] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[3][1][10:17]), '%H:%M:%S'):
            # await message.answer(f'Сейчас пара: {(str(timetable[day][1]))[20:]}, пара номер 1, до конца пары .')
            #await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')
            endTime = datetime.datetime.strptime(str(timetable[day][1][10:17]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №1</b>.\n<b>Название:</b> {(str(timetable[day][1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.1]))[20:]}", parse_mode = "HTML")
            
        
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[3][2.1][:7] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[3][2.1][10:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.1]))[20:]}, пара номер 2, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][2.1][10:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.2]))[20:]}", parse_mode = "HTML")
            
        
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[3][2.2][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[3][2.2][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.2]))[20:]}, пара номер 2, до конца пары .')

            endTime = datetime.datetime.strptime(str(timetable[day][2.2][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.2]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][3]))[20:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[3][3][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[3][3][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][3]))[20:]}, пара номер 3, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][3][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №3</b>.\n<b>Название:</b> {(str(timetable[day][3]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][4]))[20:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[3][4][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[3][4][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][4]))[20:]}, пара номер 4, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][4][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №4</b>.\n<b>Название:</b> {(str(timetable[day][4]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.", parse_mode = "HTML")
            
        
        else: 
            await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')

    elif day == 4:
        if datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[4][1][:7] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[4][1][10:17]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][1]))[20:]}, пара номер 1, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][1][10:17]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №1</b>.\n<b>Название:</b> {(str(timetable[day][1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.1]))[20:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[4][2.1][:7] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[4][2.1][10:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.1]))[20:]}, пара номер 2, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][2.1][10:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.2]))[20:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[4][2.2][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[4][2.2][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.2]))[20:]}, пара номер 2, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][2.2][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.2]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][3]))[20:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[4][3][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[4][3][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][3]))[20:]}, пара номер 3, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][3][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №3</b>.\n<b>Название:</b> {(str(timetable[day][3]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][4]))[20:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[4][4][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[4][4][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][4]))[20:]}, пара номер 4, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][4][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №4</b>.\n<b>Название:</b> {(str(timetable[day][4]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.", parse_mode = "HTML")
            
        else: 
            await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')

    elif day == 5:
        if datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[2][1][:7] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[2][1][10:17]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][1]))[20:]}, пара номер 1, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][1][10:17]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №1</b>.\n<b>Название:</b> {(str(timetable[day][1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.1]))[20:]}", parse_mode = "HTML")
            
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[5][2.1][:7] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[5][2.1][10:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.1]))[20:]}, пара номер 2, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][2.1][10:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.1]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][2.2]))[20:]}", parse_mode = "HTML")
            
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[5][2.2][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[5][2.2][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][2.2]))[20:]}, пара номер 2, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][2.2][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №2</b>.\n<b>Название:</b> {(str(timetable[day][2.2]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][3]))[20:]}", parse_mode = "HTML")
            

        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[5][3][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[5][3][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][3]))[20:]}, пара номер 3, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][3][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №3</b>.\n<b>Название:</b> {(str(timetable[day][3]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.\n\n<b>Следующая пара:</b> {(str(timetable[day][4]))[20:]}", parse_mode = "HTML")
            
        elif datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') >= datetime.datetime.strptime(str( timetable[5][4][:8] ), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], '%H:%M:%S') < datetime.datetime.strptime(str(timetable[5][4][11:18]), '%H:%M:%S'):
            #await message.answer(f'Сейчас пара: {(str(timetable[day][4]))[20:]}, пара номер 4, до конца пары .')
            endTime = datetime.datetime.strptime(str(timetable[day][4][11:18]), '%H:%M:%S')
            timeToEndRemain = TimeCalc(endTime, timeNow)

            await message.answer(f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №4</b>.\n<b>Название:</b> {(str(timetable[day][4]))[20:]}\n<b>До конца пары осталось:</b> {timeToEndRemain}.", parse_mode = "HTML")
            

        else: 
            await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')

    else: 
            await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')


    

if __name__ == '__main__':
    from handlers import dp
 
    executor.start_polling(dp, skip_updates=True)