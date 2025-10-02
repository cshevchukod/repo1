print("Hello World")

print("Hello Git")

print("Hello Git 2")

name = 'Kostiantyn'
age = 39
#print(name, age)

rate = 1
value_day = 100
value_night = 50
rate_night = rate / 2
payment = (rate * value_day) + (rate_night *value_night)
#print (payment)

length = "2.75"
width = "1.75"
area = float(length)*float(width)
show = f"With width {width} and length {length} of the room, its area is equal to {area}"
#print(show)

#name = input("Your name? ")
#email = input("Email: ")
#age = int(input("Age: "))
#height = float(input("Height: "))
#is_active = bool(input("Receive notifications from the website? "))
#print(name, email, age, height, is_active)

#length = float(input("Довжина: "))
#width = float(input("Ширина: "))
#area = round(length * width, 2)
#print (area)

#my_list = []        # створюємо порожній список

#my_list.insert(0, 2024)     # на позицію 0 додаємо ціле число
#my_list.insert(1, 'Python') # на позицію 1 додаємо рядок
#my_list.insert(2, 3.12)     # на позицію 2 додаємо дійсне число



my_list = [2024, 3.12]
some_data = ['Python']

# 1. Додаємо всі елементи зі списку some_data в my_list
my_list.extend(some_data)

# 2. Додаємо 'Python' на позицію з індексом 1
my_list.insert(1, 'Python')

# 3. Розвертаємо порядок елементів
my_list.reverse()

print(my_list)
