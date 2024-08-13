import random

# Function to quiz the user on converting declarative sentences to questions
def question_maker(sentences, num_questions):
    random.shuffle(sentences)
    selected_sentences = sentences[:num_questions]
    score = 0
    for declarative, question in selected_sentences:
        answer = input(f"What is the question form of: '{declarative}' ")
        if answer.lower() == question.lower():
            print("\033[92mCorrect!\033[0m")  # Green text
            score += 1
        else:
            print(f"\033[91mWrong! The correct answer is '{question}'.\033[0m")  # Red text
    print(f"Your final score is {score}/{num_questions}.")
