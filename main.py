import calendar
import json
import datetime
# .
# .
# .

# Команда, которая выводит какая сейчас пара, номер пары, сколько времени до коцна пары.

timeNow = datetime.datetime.now()
day = datetime.datetime.isoweekday(datetime.datetime.now())



data = {
    5: {
        4: "13:40:00 - 15:00:00 | Тестирование"
    }
}

def TimeCalc(end, now):
    return str(end - now)[13:17]

if day == 5: 
    if int(str(timeNow)[11:-13]) > 13 and int(str(timeNow)[11:-13]) < 15:
        endTime = data[5][4][11:19]
        endTime = datetime.datetime.strptime(endTime, '%H:%M:%S')
        print(f'Сейчас пара: {(str(data[5][4]))[22:]}, пара номер 4, до конца пары {TimeCalc(endTime, timeNow)}.')
