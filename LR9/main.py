# Створення файлу TF4_1
with open("TF4_1.txt", "w") as file_tf4_1:
  file_tf4_1.write("apple banana orange\n")
  file_tf4_1.write("cat dog mouse\n")
  file_tf4_1.write("hello world\n")
  file_tf4_1.write("python programming is fun\n")

# Аналіз файлу TF4_1 та запис результатів у файл TF4_2
word_length_counts = {}
with open("TF4_1.txt", "r") as file_tf4_1:
  for line in file_tf4_1:
    words = line.split()
    for word in words:
      word_length = len(word)
      if word_length in word_length_counts:
        word_length_counts[word_length] += 1
      else:
        word_length_counts[word_length] = 1

with open("TF4_2.txt", "w") as file_tf4_2:
  for word_length, count in sorted(word_length_counts.items()):
    file_tf4_2.write(f"Слова з {word_length} символами: {count}\n")

# Виведення результатів з файлу TF4_2
with open("TF4_2.txt", "r") as file_tf4_2:
  for line in file_tf4_2:
    print(line, end="")
