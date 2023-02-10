import calendar
import json
import datetime
# .
# .
# .

# Команда, которая выводит какая сейчас пара, номер пары, сколько времени до коцна пары.

timeNow = datetime.datetime.now()
day = datetime.datetime.isoweekday(datetime.datetime.now())



timetable = {
    1: {
        1: "8:50:00 - 10:20:00 | Технический английский",
        2.1: "10:40:00 - 11:25:00 | Тестирование ПО (Толмачёва)",
        2.2: "11:45:00 - 12:30:00 | Тестирование ПО (Толмачёва)"
        3: "12:40:00 - 14:10:00 | Блокчейн",
        4: "14:20:00 - 15:50:00 | Английский язык",
    }, 
    2: {
        1: "8:00:00 - 9:30:00 | JavaScript",
        2.1: "9:40:00 - 10:25:00 | JavaScript",
        2.2: "10:45:00 - 11:30:00 | JavaScript",
        3: "11:50:00 - 13:20:00 | Python",
        4: ""
    }, 
    3: {
    }, 
    4: {
    }
    5: {
        4: "13:40:00 - 15:00:00 | Тестирование"
    }
}

def TimeCalc(end, now):
    return str(end - now)[13:17]

if day == 5: 
    if int(str(timeNow)[11:-13]) > 13 and int(str(timeNow)[11:-13]) < 15:
        endTime = timetable[5][4][11:19]
        endTime = datetime.datetime.strptime(endTime, '%H:%M:%S')
        print(f'Сейчас пара: {(str(timetable[5][4]))[22:]}, пара номер 4, до конца пары {TimeCalc(endTime, timeNow)}.')
