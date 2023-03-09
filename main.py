from aiogram import Bot, Dispatcher, executor, types
import calendar
import json
import datetime

#
#
#

with open("token.json", "r") as file:
    tokenfile = json.load(file)

TOKEN = tokenfile["token"]

bot = Bot(token = TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands = ['lesson'])
async def send_lesson(message: types.Message):
    timeNow = datetime.datetime.now()
    day = datetime.datetime.isoweekday(datetime.datetime.now())

    with open("jsons/timetable.json", "r", encoding = "UTF-8") as file:
        timetable = json.load(file)

    def timeForLessonEnd(end, now):
        return f'{((str(end - now)[13:])[:-13])} час(a/ов) и {int((str(end - now)[15:])[:-10]) + 1} минут(а/ы)'

    def sendCommand(number, name, endtime, classroom, nextlesson):
        return f"<u><b>Вот информация о текущей паре:</b></u>\n\n<b>Курс:</b> ИСиП(п) 2/3. <b>Пара №{number[0]}</b>.\n<b>Название:</b> {name}.\n<b>Номер кабинета:</b> {classroom}.\n<b>До конца пары осталось:</b> {endtime}.\n\n<b>Следующая пара:</b> {nextlesson}."

    def specTimefunc():
        minuteList = ['а', 'ы', 'ы', 'ы', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', 'а', 'ы', 'ы', 'ы', '', '', '', '', '', '', 'а', 'ы', 'ы', '', '', '', '', '', '', '', 'а', 'ы', 'ы', '', '', '', '', '', '', '', 'а', 'ы', 'ы', '', '', '', '', '', '', '']
        hoursList = ['', 'а', 'а', 'а', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', 'ов', '', 'а', 'а', 'а']

        message = f"""На данный момент пары не идут.
        
Текущая дата: {str(timeNow)[8:10]}.{str(timeNow)[5:7]}.{str(timeNow)[:4]}.   
Текущее время: {str(timeNow.hour)} час{hoursList[timeNow.hour - 1]} {str(timeNow.minute)} минут{minuteList[timeNow.minute - 1]}.
"""

        return message


    if day == 6 or day == 7:
        await message.answer(specTimefunc())
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

        with open("jsons/main.json", "r") as f:
            table = json.load(f)

        lessonNumber = "3"
        lessonName = timetable[str(day)][lessonNumber]["lessonName"]
        lessonEndTime = timeForLessonEnd(endTime, timeNow)
        lessonClassroom = timetable[str(day)][lessonNumber]["classRoom"]
        nextLessonName = timetable[str(day)]["4"]["lessonName"]

        if day == 4 and table["key"] == 2:
            lessonName = timetable[str(day)][lessonNumber]["lessonNameDen"]
            lessonClassroom = timetable[str(day)][lessonNumber]["classRoomDen"]

        await message.answer(sendCommand(lessonNumber, lessonName, lessonEndTime, lessonClassroom, nextLessonName), parse_mode = "HTML")

        return

    if datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") >= datetime.datetime.strptime(str(timetable[str(day)]["4"]["startTime"]), '%H:%M:%S') and datetime.datetime.strptime(str(timeNow)[11:19], "%H:%M:%S") <= datetime.datetime.strptime(str(timetable[str(day)]["4"]["endTime"]), '%H:%M:%S'):
        endTime = datetime.datetime.strptime(str(timetable[str(day)]["4"]["endTime"]), "%H:%M:%S")

        with open("jsons/main.json", "r") as f:
            table = json.load(f)

        lessonNumber = "4"
        lessonName = timetable[str(day)][lessonNumber]["lessonName"]
        lessonEndTime = timeForLessonEnd(endTime, timeNow)
        lessonClassroom = timetable[str(day)][lessonNumber]["classRoom"]
        nextLessonName = "-"

        if day == 2 and table["key"] == 2:
            lessonName = timetable[str(day)][lessonNumber]["lessonNameDen"]
            lessonClassroom = timetable[str(day)][lessonNumber]["classRoomDen"]
        elif day == 5 and table["key"] == 2:
            lessonName = timetable[str(day)][lessonNumber]["lessonNameDen"]
            lessonClassroom = timetable[str(day)][lessonNumber]["classRoomDen"]

        await message.answer(sendCommand(lessonNumber, lessonName, lessonEndTime, lessonClassroom, nextLessonName), parse_mode = "HTML")

        return
    
    else: 
        await message.answer(specTimefunc())
        return
    


    

if __name__ == '__main__':
    from handlers import dp
 
    executor.start_polling(dp, skip_updates=True)