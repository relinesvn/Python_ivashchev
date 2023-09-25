def count_vowels_and_consonants(text):
    vowels = "aeiouy"
    text = text.lower()  # Перетворимо текст у нижній регістр для порівняння

    vowel_count = 0
    consonant_count = 0

    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count

# Запитуємо користувача ввести текст
text = input("Введіть текст: ")

# Викликаємо функцію для обчислення кількості голосних та приголосних літер
vowel_count, consonant_count = count_vowels_and_consonants(text)

# Визначаємо, які літери - голосні або приголосні - більше у тексті
if vowel_count > consonant_count:
    print("Голосних літер більше у тексті.")
    print("Голосні літери у тексті:", set(filter(lambda x: x in "aeiouy", text.lower())))
elif vowel_count < consonant_count:
    print("Приголосних літер більше у тексті.")
    print("Приголосні літери у тексті:", set(filter(lambda x: x.isalpha() and x not in "aeiouy", text.lower())))
else:
    print("Кількість голосних і приголосних літер однакова у тексті.")
