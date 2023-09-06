# Розмір масиву
n = 7

# Створюємо порожній двовимірний масив з нулями
array = [[0 for _ in range(n)] for _ in range(n)]

# Заповнюємо масив відповідно до умови
for i in range(n):
    for j in range(i, n):
        array[i][j] = j - i + 1

# Виводимо масив
for row in reversed(array):
    print(' '.join(map(str, row)))
