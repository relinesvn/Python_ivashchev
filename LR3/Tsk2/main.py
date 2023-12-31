# Запитуємо користувача ввести слово
word = input("Введіть слово: ")

# Ініціалізуємо порожній список для зберігання повторюючихся літер
duplicates = []

# Створюємо словник для зберігання кількості входжень кожної літери
letter_counts = {}

# Перебираємо кожну літеру в слові
for letter in word:
  # Перевіряємо, чи ця літера вже була в слові
  if letter in letter_counts:
    # Якщо так, збільшуємо кількість входжень
    letter_counts[letter] += 1
  else:
    # Якщо літера вперше зустрілася, додаємо її до словника
    letter_counts[letter] = 1

# Перевіряємо кожну літеру, що зустрічається більше одного разу і додаємо їх до списку duplicates
for letter, count in letter_counts.items():
  if count > 1:
    duplicates.append(letter)

# Виводимо літери, які зустрічаються більше одного разу
if len(duplicates) > 0:
  print("Літери, які зустрічаються більше одного разу:", ', '.join(duplicates))
else:
  print("У введеному слові немає повторюючихся літер.")
