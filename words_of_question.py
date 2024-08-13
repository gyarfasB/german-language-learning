import random

# Function to quiz the user on German words
def words_of_question(sentences, num_questions):
    random.shuffle(sentences)
    selected_sentences = sentences[:num_questions]
    score = 0
    for sentence, word in selected_sentences:
        answer = input(f"{sentence}")
        if answer.lower() == word.lower():
            print("\033[92mCorrect!\033[0m")  # Green text
            score += 1
        else:
            print(f"\033[91mWrong! The correct answer is '{word}'.\033[0m")  # Red text
    print(f"Your final score is {score}/{num_questions}.")
