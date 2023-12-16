import numpy as np
import json


def read_matrices_from_json(filename):
  """
    Зчитує матриці з файлу JSON та повертає їх у вигляді списку NumPy масивів.

    Parameters:
    filename (str): Ім'я файлу, з якого зчитується матриці у форматі JSON.

    Returns:
    list of np.ndarray: Список матриць у форматі NumPy або None, якщо виникла помилка.
    """
  try:
    with open(filename, 'r') as file:
      # Завантаження JSON-даних з файлу
      data = json.load(file)

      # Створення списку матриць
      matrices = [np.array(matrix) for matrix in data['matrices']]
      return matrices
  except FileNotFoundError:
    print(f"Файл {filename} не знайдено.")
    return None
  except Exception as e:
    print(f"Помилка при зчитуванні матриць з файлу: {e}")
    return None


def write_result_to_file(result_matrix, output_filename="out.txt"):
  """
    Записує результат обчислення до файлу.

    Parameters:
    result_matrix (np.ndarray): Результат обчислення у форматі NumPy масиву.
    output_filename (str): Ім'я вихідного файлу.

    Returns:
    None
    """
  try:
    with open(output_filename, 'w') as file:
      # Запис результату у файл
      file.write("Результат обчислення:\n")
      file.write(str(result_matrix))
    print(f"Результат записано у файл {output_filename}")
  except Exception as e:
    print(f"Помилка при записі результату у файл: {e}")


def main():
  # Ім'я файлу з матрицями у форматі JSON
  file_name = "matrix.json"

  # Зчитування матриць з файлу
  matrices = read_matrices_from_json(file_name)

  if matrices is None:
    return

  if not matrices:
    print("Файл не містить матриць для обробки.")
    return

  # Вибір операції користувачем
  operation = input(
      "\nВиберіть операцію (додавання - 'add', віднімання - 'subtract', множення - 'multiply'): "
  )

  try:
    # Виконання вибраної операції
    if operation == 'add':
      result_matrix = np.add(matrices[0], matrices[1])
    elif operation == 'subtract':
      result_matrix = np.subtract(matrices[0], matrices[1])
    elif operation == 'multiply':
      result_matrix = np.dot(matrices[0], matrices[1])
    else:
      print("Невірна операція. Завершення програми.")
      return

    # Запис результату у файл
    write_result_to_file(result_matrix)
  except ValueError as ve:
    print(f"Помилка: {ve}")


if __name__ == "__main__":
  main()
