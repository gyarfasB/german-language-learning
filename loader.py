import csv

# Function to load words from a CSV file
def load_words(file_path):
    words = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            words.append((row['German'], row['English']))
    return words

# Function to load sentences from a CSV file
def load_sentences(file_path):
    sentences = []
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            sentences.append((row['Declarative'], row['Question']))
    return sentences

# Function to load sentences from a CSV file
def load_questions(file_path):
    questionwords = []
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            questionwords.append((row['Question Sentence'], row['Missing word']))
    return questionwords