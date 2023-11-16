import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer, WordNetLemmatizer
import string

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


def process_text(input_text):
  # Токенізація по словам
  tokens = word_tokenize(input_text)

  # Лемматизація
  lemmatizer = WordNetLemmatizer()
  lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]

  # Стеммінг
  stemmer = PorterStemmer()
  stemmed_tokens = [stemmer.stem(token) for token in tokens]

  # Видалення стоп-слів
  stop_words = set(stopwords.words('english'))
  filtered_tokens = [
      token for token in lemmatized_tokens if token.lower() not in stop_words
  ]

  # Видалення пунктуації
  filtered_tokens = [
      token for token in filtered_tokens if token not in string.punctuation
  ]

  # Повернення обробленого тексту
  processed_text = ' '.join(filtered_tokens)
  return processed_text


def main():
  # Зчитування тексту з файлу
  with open('input.txt', 'r', encoding='utf-8') as file:
    input_text = file.read()

  # Обробка тексту
  processed_text = process_text(input_text)

  # Запис обробленого тексту у файл
  with open('output.txt', 'w', encoding='utf-8') as file:
    file.write(processed_text)


if __name__ == "__main__":
  main()
