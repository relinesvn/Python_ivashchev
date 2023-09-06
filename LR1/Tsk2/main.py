# Ініціалізуємо змінні для перших двох чисел Фібоначчі
prev = 0
current = 1

# Ініціалізуємо змінну для суми перших 8 чисел Фібоначчі
sum_fibonacci = 0

# Змінна, щоб відстежити кількість знайдених чисел Фібоначчі
count = 0

# Використовуємо цикл while для знаходження та друку перших 8 чисел Фібоначчі
while count < 8:
    # Виводимо поточне число Фібоначчі
    print(current, end=' ')

    # Додаємо поточне число до суми
    sum_fibonacci += current

    # Обчислюємо наступне число Фібоначчі і поновлюємо значення змінних
    temp = current
    current = prev + current
    prev = temp

    # Збільшуємо лічильник знайдених чисел Фібоначчі
    count += 1

# Друкуємо суму перших 8 чисел Фібоначчі
print("\nСума перших 8 чисел Фібоначчі:", sum_fibonacci)