def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  num_words = get_num_words(text)
  num_of_characters = get_num_times_character(text)

  create_report(num_words, num_of_characters)

def get_num_words(text):
  words = text.split()
  return len(words)

def get_book_text(path):
  with open(path) as f:
    return f.read()

def get_num_times_character(text):
  char_counts = {}

  for character in text:
    char = character.lower()

    if char not in char_counts:
      char_counts[char] = 1
    char_counts[char] += 1
  
  return char_counts

def create_report(num_words, num_of_characters):
  word_string = f"{num_words} words found in the document"
  char_list = list()

  for key, value in num_of_characters.items():
    if key.isalpha():
      char_list.append(f"The '{key}' character was found {value} times")

  print(word_string)

  char_list.sort()
  
  for item in char_list:
    print(item)

main()