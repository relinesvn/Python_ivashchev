import sports_module  # Підключаємо модуль sports_module


def main():
  # Функція для обчислення сумарного шляху
  n = int(input("Введіть кількість днів для обчислення сумарного шляху: "))
  result_distance = sports_module.calculate_total_distance(n)
  print(f"Сумарний шлях спортсмена за {n} днів: {result_distance:.2f} км")


if __name__ == "__main__":
  main()
