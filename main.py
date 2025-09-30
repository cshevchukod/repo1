print("Hello World")

print("Hello Git")

print("Hello Git 2")

def is_adult(age):
    return age >= 18

# Виклик функції, який поверне True або False
can_vote = is_adult(17) 
print(can_vote)  # Виведе: True

menu_dict = {"sandwiches": 6, "wraps": 4, "soup": 1}
user_dict = {"name": "Wendy", "active": False, "followers": 2}
print (user_dict)

name = 'Wendy\\s dog'
print(name)   # Wendy's dog

var1 = 12 + 34      # вираз
var2 = len("hello") # вираз
print(var1, var2)

x = 5.0
y = -1.25
z = 587643291.001

# Приклад 1: Перебір елементів списку
menu = ["wraps", "sandwiches", "soup", "salad"]
print("Our menu:")
for item in menu:
    print(item)


# Приклад 2: Перебір ключів словника
user_profile = {"name": "Wendy", "status": "active"}
print("\nUser data:")
for key in user_profile:
    print(f"{key}: {user_profile[key]}")

name = input("What’s your name? ")

var1 = len("hello")       # 5
var2 = len(["hi", "hello", "ola"])  # 3

menu_items = ["wrap", "salad", "sandwich", "soup"]

print("Hello! " + name + ". How are you?")

def greet():
    return "Hello"

print(greet(), "Wendy")  # Hello Wendy

age = int(input("How old are you now? "))
print("Next year you will be:", age + 1)

# ✅ Гарні, зрозумілі назви:
user_name = "wendy"
lucky_number = 7
best_pet = "porcupine"


# ❌ Погані назви (варто уникати):
n = "wendy"                # неінформативна, незрозуміло, що означає "n"
user_age = "twenty"        # вводить в оману (назва натякає на число, а зберігається рядок)
BestPet = "porcupine"      # порушує стиль (назви змінних не починають з великої літери)

my_lucky_number = 7
guess = int(input("Guess my lucky number: "))
while my_lucky_number != guess:
    guess = int(input("Oops! Not it. Try again: "))
print("Congrats! You guessed it.")
