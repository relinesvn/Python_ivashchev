# Запитуємо користувача ввести рядок
my_string = input("Введіть рядок: ")

# Перевіряємо, чи довжина рядка дозволяє виконати зріз
if len(my_string) >= 15:
  # Отримуємо зріз від 12-го символа до 15-го
  substring = my_string[11:15]
  # Виводимо отриманий зріз
  print("Отриманий зріз:", substring)
else:
  print("Рядок занадто короткий для виконання операції зрізу.")