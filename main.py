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
# timetable = {
#     1: {
#         1: "8:50:00 - 10:20:00 | Технический иностранный.",
#         2.1: "10:40:00 - 11:25:00 | Поддержка и тестирование программных модулей.",
#         2.2: "11:45:00 - 12:30:00 | Поддержка и тестирование программных модулей.",
#         3: "12:40:00 - 14:10:00 | Разработка программных решений (Blockchain).",
#         4: "14:20:00 - 15:50:00 | Иностранный язык.",
#     }, 
#     2: {
#         1: "8:00:00 - 9:30:00 | Объектно-ориентировочный язык программирования JavaScript.",
#         2.1: "9:40:00 - 10:25:00 | Объектно-ориентировочный язык программирования JavaScript.",
#         2.2: "10:45:00 - 11:30:00 | Объектно-ориентировочный язык программирования JavaScript.",
#         3: "11:50:00 - 13:20:00 | Основы алгоритмизации и программирования.",
#         4: "13:30:00 - 15:00:00 | Архитектура аппаратных средств."
#     }, 
#     3: {
#         1: "8:00:00 - 9:30:00 | Пара отдыха (дома).",
#         2.1: "9:40:00 - 10:25:00 | Основы алгоритмизации и программирования.",
#         2.2: "10:45:00 - 11:30:00 | Основы алгоритмизации и программирования.",
#         3: "11:50:00 - 13:20:00 | Физическая культура.",
#         4: "13:30:00 - 15:00:00 | Безопасность жизнедеятельности."
#     }, 
#     4: {
#         1: "8:00:00 - 9:30:00 | Технология разработки и защиты баз данных.",
#         2.1: "9:40:00 - 10:25:00 | Теория вероятности и математическая статистика.",
#         2.2: "10:45:00 - 11:30:00 | Теория вероятности и математическая статистика.",
#         3: "11:50:00 - 13:20:00 | Технология разработки и защиты баз данных. / Объектно-ориентировочный язык программирования JavaScript.",
#         4: "13:30:00 - 15:00:00 | Поддержка и тестирование программных модулей."
#     },
#     5: {
#         1: "8:00:00 - 9:30:00 | Архитектура аппаратных средств.",
#         2.1: "9:40:00 - 10:25:00 | Компьютерные сети.",
#         2.2: "10:45:00 - 11:30:00 | Компьютерные сети.",
#         3: "11:50:00 - 13:20:00 | Элементы высшей математики.",
#         4: "13:30:00 - 15:00:00 | Безопасность жизнедеятельности. / Поддержка и тестирование программных модулей."
#     }
# }

with open("token.json", "r") as file:
    tokenfile = json.load(file)

TOKEN = tokenfile["token"]

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


timeNow = datetime.datetime.now()
day = datetime.datetime.isoweekday(datetime.datetime.now())

@dp.message_handler(commands = ['lesson'])
async def send_lesson(message: types.Message):
    with open("jsons/timetable.json", "r", encoding = "UTF-8") as file:
        timetable = json.load(file)

    def timeForLessonEnd(end, now):
        return f'{((str(end - now)[13:])[:-13])} час(a/ов) и {int((str(end - now)[15:])[:-10]) + 1} минут(а/ы)'

    def sendCommand(number, name, endtime, classroom, nextlesson):
        return f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №{number[0]}</b>.\n<b>Название:</b> {name}.\n<b>Номер кабинета:</b> {classroom}.\n<b>До конца пары осталось:</b> {endtime}.\n\n<b>Следующая пара:</b> {nextlesson}."

    if day == 6 or day == 7:
        await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')
        return

    if datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") >= datetime.datetime.strptime(str(timetable[str(day)]["1"]["startTime"]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") <= datetime.datetime.strptime(str(timetable[str(day)]["1"]["endTime"]), '%H:%M:%S'):
        endTime = datetime.datetime.strptime(str(timetable[str(day)]["1"]["endTime"]), "%H:%M:%S")

        lessonNumber = "1"
        lessonName = timetable[str(day)][lessonNumber]["lessonName"]
        lessonEndTime = timeForLessonEnd(endTime, timeNow)
        lessonClassroom = timetable[str(day)][lessonNumber]["classRoom"]
        nextLessonName = timetable[str(day)]["2.1"]["lessonName"]

        await message.answer(sendCommand(lessonNumber, lessonName, lessonEndTime, lessonClassroom, nextLessonName), parse_mode = "HTML")

        return

    if datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") >= datetime.datetime.strptime(str(timetable[str(day)]["2.1"]["startTime"]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") <= datetime.datetime.strptime(str(timetable[str(day)]["2.1"]["endTime"]), '%H:%M:%S'):
        endTime = datetime.datetime.strptime(str(timetable[str(day)]["2.1"]["endTime"]), "%H:%M:%S")

        lessonNumber = "2.1"
        lessonName = timetable[str(day)][lessonNumber]["lessonName"]
        lessonEndTime = timeForLessonEnd(endTime, timeNow)
        lessonClassroom = timetable[str(day)][lessonNumber]["classRoom"]
        nextLessonName = timetable[str(day)]["2.2"]["lessonName"]

        await message.answer(sendCommand(lessonNumber, lessonName, lessonEndTime, lessonClassroom, nextLessonName), parse_mode = "HTML")

        return
    
    if datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") >= datetime.datetime.strptime(str(timetable[str(day)]["2.2"]["startTime"]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") <= datetime.datetime.strptime(str(timetable[str(day)]["2.2"]["endTime"]), '%H:%M:%S'):
        endTime = datetime.datetime.strptime(str(timetable[str(day)]["2.2"]["endTime"]), "%H:%M:%S")

        lessonNumber = "2.2"
        lessonName = timetable[str(day)][lessonNumber]["lessonName"]
        lessonEndTime = timeForLessonEnd(endTime, timeNow)
        lessonClassroom = timetable[str(day)][lessonNumber]["classRoom"]
        nextLessonName = timetable[str(day)]["3"]["lessonName"]

        await message.answer(sendCommand(lessonNumber, lessonName, lessonEndTime, lessonClassroom, nextLessonName), parse_mode = "HTML")

        return

    if datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") >= datetime.datetime.strptime(str(timetable[str(day)]["3"]["startTime"]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") <= datetime.datetime.strptime(str(timetable[str(day)]["3"]["endTime"]), '%H:%M:%S'):
        endTime = datetime.datetime.strptime(str(timetable[str(day)]["3"]["endTime"]), "%H:%M:%S")

        lessonNumber = "3"
        lessonName = timetable[str(day)][lessonNumber]["lessonName"]
        lessonEndTime = timeForLessonEnd(endTime, timeNow)
        lessonClassroom = timetable[str(day)][lessonNumber]["classRoom"]
        nextLessonName = timetable[str(day)]["4"]["lessonName"]

        await message.answer(sendCommand(lessonNumber, lessonName, lessonEndTime, lessonClassroom, nextLessonName), parse_mode = "HTML")

        return

    if datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") >= datetime.datetime.strptime(str(timetable[str(day)]["4"]["startTime"]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") <= datetime.datetime.strptime(str(timetable[str(day)]["4"]["endTime"]), '%H:%M:%S'):
        endTime = datetime.datetime.strptime(str(timetable[str(day)]["4"]["endTime"]), "%H:%M:%S")

        lessonNumber = "4"
        lessonName = timetable[str(day)][lessonNumber]["lessonName"]
        lessonEndTime = timeForLessonEnd(endTime, timeNow)
        lessonClassroom = timetable[str(day)][lessonNumber]["classRoom"]
        nextLessonName = "-"

        await message.answer(sendCommand(lessonNumber, lessonName, lessonEndTime, lessonClassroom, nextLessonName), parse_mode = "HTML")

        return
    
    else: 
        await message.answer(f'☺️ Сейчас отдых. Текущая дата: {str(timeNow)[:4]} год, {str(timeNow)[5:7]} месяц, {str(timeNow)[8:10]} число.')
        return
    


    

if __name__ == '__main__':
    from handlers import dp
 
    executor.start_polling(dp, skip_updates=True)