
this_is_string = "Hi there!"

the_same_string = 'Hi there!'

this_is_string == the_same_string # True

text = """This is first line
And second line
Last third line"""

song = '''Jingle bells, jingle bells
Jingle all the way
Oh, what fun it is to ride
In a one horse open sleigh'''

print(this_is_string, the_same_string, text, song, end=", \n")

one_line_text = "Textual data in Python is handled with str objects," \
                " or strings. Strings are immutable sequences of Unicode" \
                " code points. String literals are written in a variety " \
                " of ways: single quotes, double quotes, triple quoted."
print(one_line_text)

print('')

text = "hello world"
result = text.split()
print(result)  # Виведе: ['hello', 'world']
print(text)

text = "apple,banana,cherry"
result = text.split(',')
print(result)  # Виведе: ['apple', 'banana', 'cherry']
print(text)

list_of_strings = ['Hello', 'world']
result = ' '.join(list_of_strings) + "!"
print(result)  # Виведе: 'Hello world'

elements = ['earth', 'air', 'fire', 'water']
result = ', '.join(elements)
print(result)  # Виведе: 'earth, air, fire, water'

clean = ' ,  spacious  , '.strip()
print(clean) # spacious

text = "Hello world"
new_text = text.replace("world", "Python")
print(new_text)

text = "one fish, two fish, red fish, blue fish"
new_text = text.replace("fish", "bird", 2)
print(new_text)

print('')

test_hook = 'TestHook'

print(test_hook.removeprefix('Test')) # Hook
print(test_hook.removeprefix('Hook')) # TestHook
print(test_hook.removesuffix('Test')) # TestHook
print(test_hook.removesuffix('Hook')) # Test

print('')

url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
_, query = url_search.split('?')
print(query)

obj_query = {}
for el in query.split('&'):
    print(el)
    key, value = el.split('=')
    obj_query.update({key: value.replace('+', ' ')})
print(obj_query)

print('')

number = "12345"
print(number.isdigit())  # Виведе: True

text = "Number123"
print(text.isdigit())  # Виведе: False

for char in "Hello 123":
    if char.isdigit():
        print(f"'{char}' - цифра")
    else:
        print(f"'{char}' - не цифра")

print('')

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)
print('')
print('')
print('')

str = "This is string example"
print(str.translate(trantab))

import random

# Глобальний генератор
print("global:", random.random())  

# Локальний із seed
rng = random.Random(42)
print("rng:", rng.random())
print("rng:", rng.random())
print(rng)

print('')

symbols = "0123456789ABCDEF"
code = [
        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
        ]

MAP = {}

for s, c in zip(symbols, code):
    MAP[ord(s)] = c
    MAP[ord(s.lower())] = c

print(MAP)
result = "34 DF 56 AC".translate(MAP)
print(result)

MAP = {ord('A'): '1', ord('a'): '2'}

print("Aa".translate(MAP))

s = "education"

auto = str.maketrans("aeiou", "12345")
manual = {97: "1", 101: "2", 105: "3", 111: "4", 117: "5"}

print(s.translate(auto))   # 2d5c1t34n
print(s.translate(manual)) # 2d5c1t34n

print('')

for i in range(20):
    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
    print(s)

value = 0.123
print (f"{value:%}")

print('')

import re

text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")

text = "Вивчення Python може бути веселим."
pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())

print('')

email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)"
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)

print('')

phone = """Михайло Куліш: 050-171-1634
Вікторія Кущ: 063-134-1729
Оксана Гавриленко: 068-234-5612"""
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)

text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.span())
    print("Знайдено:", match.string)
    print("Знайдено:", match.group())
    print("Знайдено:", match)
else:
    print("Не знайдено.")