def find_sequence_in_list(input_list, sequence):
  found_indices = []

  for i in range(len(input_list) - len(sequence) + 1):
    if input_list[i:i + len(sequence)] == sequence:
      found_indices.append(i)

  return found_indices


def print_list(input_list):
  print("Список:", input_list)


# Запитуємо користувача ввести список
user_list = input("Введіть список (елементи розділіть пробілами): ").split()

# Запитуємо користувача ввести послідовність для пошуку (розділіть пробілами)
sequence_to_find = input(
    "Введіть послідовність для пошуку (елементи розділіть пробілами): ").split(
    )

# Перетворюємо введені рядки в списки цілих чисел (або може бути рядками, в залежності від введення)
try:
  user_list = [int(item) for item in user_list]
  sequence_to_find = [int(item) for item in sequence_to_find]
except ValueError:
  pass  # Продовжуємо якщо не вдалося перетворити всі елементи в цілі числа

# Викликаємо функцію для пошуку послідовності у списку
found_indices = find_sequence_in_list(user_list, sequence_to_find)

# Викликаємо функцію для виведення списку на екран
print_list(user_list)

# Виводимо знайдені індекси послідовності
if found_indices:
  print(f"Послідовність {sequence_to_find} знайдена в списку на позиціях:",
        found_indices)
else:
  print(f"Послідовність {sequence_to_find} не знайдена в списку.")
