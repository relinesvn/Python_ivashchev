import math


def calculate_z(m):
  if m < -2:
    print("Помилка: m має бути більше або дорівнювати -2.")
    return None
  z = 1 / math.sqrt(m + 2)
  return z


def calculate_total_distance(n):
  distance = 10  # Перший день пробігає 10 км
  total_distance = 10  # Початкова сумарна відстань
  for day in range(2, n + 1):
    distance *= 1.10  # Збільшуємо денну норму на 10%
    total_distance += distance
  return total_distance


# Функція для обчислення z
m = float(input("Введіть значення m: "))
result_z = calculate_z(m)
if result_z is not None:
  print(f"Результат функції z: {result_z:.2f}")

# Функція для обчислення сумарного шляху
n = int(input("Введіть кількість днів для обчислення сумарного шляху: "))
result_distance = calculate_total_distance(n)
print(f"Сумарний шлях спортсмена за {n} днів: {result_distance:.2f} км")
