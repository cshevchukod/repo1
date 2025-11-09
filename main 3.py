from datetime import datetime

current_datetime_1 = datetime.now()
print(current_datetime_1.year)
print(current_datetime_1.month)
print(current_datetime_1.day)
print(current_datetime_1.hour)
print(current_datetime_1.minute)
print(current_datetime_1.second)
print(current_datetime_1.microsecond)
print(current_datetime_1.tzinfo)

print('')

current_datetime_2 = datetime.now()
print(current_datetime_2.date())
print(current_datetime_2.time())

print('')

seventh_day_2019 = datetime(year=2019, month=1, day=7, hour=14)
seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)

difference = seventh_day_2020 - seventh_day_2019
print(difference)  # 365 days, 0:00:00
print(difference.total_seconds())  # 31536000.0

print('')

from datetime import timedelta

delta = timedelta(
    days=50,
    seconds=27,
    microseconds=10,
    milliseconds=29000,
    minutes=5,
    hours=8,
    weeks=2
)
print(delta)

print('')

import datetime

# Створення об'єкта datetime з конкретною датою і часом
specific_datetime = datetime.datetime(year=2020, month=1, day=7, hour=14, minute=30, second=15)

print(specific_datetime)  # Виведе "2020-01-07 14:30:15"

print('')

from datetime import datetime, timedelta, timezone

seventh_day_2020 = datetime(year=2020, month=1, day=7, hour=14)
four_weeks_interval = timedelta(weeks=4)

print(seventh_day_2020)
print(seventh_day_2020 + four_weeks_interval)  # 2020-02-04 14:00:00
print(seventh_day_2020 - four_weeks_interval)  # 2019-12-10 14:00:00

print('')

# Створення об'єкта datetime
date = datetime(year=2023, month=12, day=18)

# Отримання порядкового номера
ordinal_number = date.toordinal()
print(f"Порядковий номер дати {date} становить {ordinal_number}")

print('')

# Встановлення дати спалення Москви Наполеоном (14 вересня 1812 року)
napoleon_burns_moscow = datetime(year=1812, month=9, day=14)

# Поточна дата
current_date = datetime.now()

# Розрахунок кількості днів
days_since = current_date.toordinal() - napoleon_burns_moscow.toordinal()
print(days_since)

print('')

now = datetime.now()

# Конвертація datetime в timestamp
timestamp = datetime.timestamp(now)
print(timestamp)  # Виведе timestamp поточного часу

print('')

now = datetime.now()

# Форматування дати і часу
formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
print(formatted_date) 

# Форматування лише дати
formatted_date_only = now.strftime("%A, %d %B %Y")
print(formatted_date_only)

# Форматування лише часу
formatted_time_only = now.strftime("%I:%M %p")
print(formatted_time_only)  

# Форматування лише дати
formatted_date_only = now.strftime("%d.%m.%Y")
print(formatted_date_only)

print('')

# Поточна дата та час
now = datetime.now()

# Конвертація у формат ISO 8601
iso_format = now.isoformat()
print(iso_format)
print(now)

print('')

iso_date_string = "2023-03-14T12:39:29.992996"

# Конвертація з ISO формату
date_from_iso = datetime.fromisoformat(iso_date_string)
print(date_from_iso)

print('')

# Створення об'єкта datetime
now = datetime.now()

# Отримання ISO календаря
iso_calendar = now.isocalendar()

print(f"ISO рік: {iso_calendar[0]}, ISO тиждень: {iso_calendar[1]}, ISO день тижня: {iso_calendar[2]}")
print(iso_calendar)

iso_calendar_1 = now.isoweekday()
print(f"Сьогодні: {iso_calendar_1}")

# Створення об'єкта datetime
now = datetime.now()

# Використання isoweekday() для отримання дня тижня
day_of_week = now.isoweekday()

print(f"Сьогодні: {day_of_week}")  # Поверне число від 1 до 7, що відповідає дню тижня

print('')

utc_time = datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)

print('')

utc_time = datetime.now(timezone.utc)

# Створення часової зони для Східного часового поясу (UTC-5)
eastern_time = utc_time.astimezone(timezone(timedelta(hours=-5)))
# Перетворює час UTC в час Східного часового поясу
print(eastern_time)  

# Припустимо, місцевий час належить до часової зони UTC+2
local_timezone = timezone(timedelta(hours=2))
local_time = datetime(year=2023, month=3, day=14, hour=12, minute=30, second=0, tzinfo=local_timezone)

# Конвертація локального часу в UTC
utc_time = local_time.astimezone(timezone.utc)
print(utc_time)  # Виведе час в UTC
print(local_timezone)
print(local_time)

iso_format_with_timezone = local_time.isoformat()
print(iso_format_with_timezone)

print('')

import time

# Записуємо час на початку виконання
start_time = time.perf_counter()

print("Початок паузи")
time.sleep(1)
print("Кінець паузи")

current_time = time.time()
print(f"Поточний час: {current_time}")

# Створюємо читабельний час через time
readable_time = time.ctime(current_time)
print(readable_time)

# Створюємо datetime з того самого timestamp
current_datetime = datetime.fromtimestamp(current_time)
print (current_datetime)

t = time.time()
print(time.ctime(t))
print(datetime.fromtimestamp(t))

current_datetime = datetime.now()
timestamp = current_datetime.timestamp()

print(current_datetime)
print(time.ctime(timestamp))

print('')

# 1️⃣ Отримуємо поточний timestamp (унікальний момент часу)
t = time.time()

# 2️⃣ Форматуємо через модуль time
formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(t))

# 3️⃣ Форматуємо через datetime (з того ж timestamp)
formatted_datetime = datetime.fromtimestamp(t).strftime("%Y-%m-%d %H:%M:%S")

# 4️⃣ Виводимо обидва результати
print("time.strftime():     ", formatted_time)
print("datetime.strftime(): ", formatted_datetime)

print('')

# Виконуємо якусь операцію
for _ in range(1_000_000):
    pass  # Просто проходить цикл мільйон разів

# Записуємо час після виконання операції
end_time = time.perf_counter()

# Розраховуємо та виводимо час виконання
execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд")

print('')

import random

dice_roll = random.randint(1, 6)
print(f"Ви кинули {dice_roll}")
cards = ["Туз", "Король", "Дама", "Валет", "10", "9", "8", "7", "6"]

random.shuffle(cards)

print(f"Перемішана колода: {cards}")

fruits = ['apple', 'banana', 'orange']
print(random.choice(fruits))

print('')

items = ['яблуко', 'банан', 'вишня', 'диня']
chosen_item = random.choices(items, k=1)
print(chosen_item) 

numbers = [1, 2, 3, 4, 5]
chosen_numbers = random.choices(numbers, k=3)
print(chosen_numbers)

colors = ['червоний', 'зелений', 'синій']
weights = [5, 10, 1]
chosen_color = random.choices(colors, weights, k=1)
print(chosen_color)

print('')

import math

# Вихідне число
x = 3.78

# Використання різних методів округлення
ceil_result = math.ceil(x)  # Округлення вгору
floor_result = math.floor(x)  # Округлення вниз
trunc_result = math.trunc(x)  # Відсікання дробової частини

print(ceil_result, floor_result, trunc_result)