def calculate_total_distance(n):
  distance = 10  # Перший день пробігає 10 км
  total_distance = 10  # Початкова сумарна відстань
  for day in range(2, n + 1):
    distance *= 1.10  # Збільшуємо денну норму на 10%
    total_distance += distance
  return total_distance
