# Запитуємо користувача ввести довжину масиву
N = int(input("Введіть довжину масиву: "))

# Ініціалізуємо пустий список для зберігання елементів масиву
array = []

# Запитуємо користувача ввести N дійсних чисел для масиву
for i in range(N):
    element = float(input(f"Введіть {i+1}-й елемент масиву: "))
    array.append(element)

# Обчислюємо середнє арифметичне від'ємних елементів
negative_sum = 0  # Зберігає суму від'ємних елементів
negative_count = 0  # Зберігає кількість від'ємних елементів

for element in array:
    if element < 0:
        negative_sum += element
        negative_count += 1

# Обчислюємо середнє арифметичне від'ємних елементів (якщо є від'ємні елементи)
if negative_count > 0:
    average_negative = negative_sum / negative_count
    print(f"Середнє арифметичне від'ємних елементів: {average_negative:.2f}")
else:
    print("У масиві немає від'ємних елементів.")
