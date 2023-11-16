import matplotlib.pyplot as plt
from collections import Counter
import string
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')


def read_text_file(file_path):
  with open(file_path, 'r', encoding='utf-8') as file:
    text = file.read()
  return text


def get_most_common_words(text, num_words=10):
  # Розділяємо текст на слова та видаляємо пунктуацію
  words = [word.strip(string.punctuation) for word in text.lower().split()]

  # Видаляємо стоп-слова
  stop_words = set(stopwords.words('english'))
  words = [word for word in words if word not in stop_words]

  # Знаходимо найбільш вживані слова
  word_counter = Counter(words)
  most_common_words = word_counter.most_common(num_words)

  return most_common_words


def plot_bar_chart(data, title):
  words, frequencies = zip(*data)

  plt.figure(figsize=(10, 6))
  plt.bar(words, frequencies, color='skyblue')
  plt.title(title)
  plt.xlabel('Words')
  plt.ylabel('Frequency')
  plt.xticks(rotation=45, ha='right')
  plt.tight_layout()
  plt.show()


def main():
  # Введення назви файлу від користувача
  file_path = input("Введіть назву текстового файлу (.txt): ")

  # Зчитування тексту з файлу
  text = read_text_file(file_path)

  # Знаходження та вивід кількості слів у тексті
  word_count = len(text.split())
  print(f"Кількість слів у тексті: {word_count}")

  # Знаходження та вивід 10 найбільш вживаних слів
  most_common_words_original = get_most_common_words(text)
  print(
      "\n10 найбільш вживаних слів у тексті (зі стоп-словами та пунктуацією):")
  for word, frequency in most_common_words_original:
    print(f"{word}: {frequency}")

  # Побудова стовпчастої діаграми для оригінального тексту
  plot_bar_chart(most_common_words_original, "Top 10 Words (Original)")

  # Видалення стоп-слів та пунктуації
  text_without_stopwords = ' '.join(
      [word for word in text.split() if word.lower() not in stop_words])

  # Знаходження та вивід 10 найбільш вживаних слів після видалення стоп-слів та пунктуації
  most_common_words_cleaned = get_most_common_words(text_without_stopwords)
  print("\n10 найбільш вживаних слів у тексті (без стоп-слів та пунктуації):")
  for word, frequency in most_common_words_cleaned:
    print(f"{word}: {frequency}")

  # Побудова стовпчастої діаграми для очищеного тексту
  plot_bar_chart(most_common_words_cleaned, "Top 10 Words (Cleaned)")


if __name__ == "__main__":
  main()
