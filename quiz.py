import random

# Function to quiz the user on German words
def quiz_user(words, num_questions):
    random.shuffle(words)
    selected_words = words[:num_questions]
    score = 0
    for german, english in selected_words:
        answer = input(f"What is the English translation of '{german}'? ")
        if answer.lower() == english.lower():
            print("\033[92mCorrect!\033[0m")  # Green text
            score += 1
        else:
            print(f"\033[91mWrong! The correct answer is '{english}'.\033[0m")  # Red text
    print(f"Your final score is {score}/{num_questions}.")
