def insert_element_into_list(input_list, element, position):
  if position < 0 or position > len(input_list):
    print("Помилка: Неправильна позиція для вставки.")
    return

  input_list.insert(position, element)


def print_list(input_list):
  print("Список:", input_list)


# Запитуємо користувача ввести список
user_list = input("Введіть список (елементи розділіть пробілами): ").split()

# Перетворюємо введений рядок в список цілих чисел (або може бути рядками, в залежності від введення)
try:
  user_list = [int(item) for item in user_list]
except ValueError:
  pass  # Продовжуємо якщо не вдалося перетворити всі елементи в цілі числа

# Запитуємо користувача ввести елемент для вставки
element_to_insert = input("Введіть елемент для вставки: ")

# Запитуємо користувача ввести позицію для вставки
position_to_insert = int(input("Введіть позицію для вставки: "))

# Викликаємо функцію для вставки елемента в список
insert_element_into_list(user_list, element_to_insert, position_to_insert)

# Викликаємо функцію для виведення списку на екран
print_list(user_list)
