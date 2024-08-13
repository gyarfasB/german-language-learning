from loader import load_words, load_sentences, load_questions
from quiz import quiz_user
from question_maker import question_maker
from words_of_question import words_of_question

# Function to handle user input for number of questions
def get_num_questions():
    while True:
        print("Choose the number of items for the game: 10, 25, 50, 100")
        try:
            num_questions = int(input("Enter the number of questions: "))
            if num_questions not in [10, 25, 50, 100]:
                raise ValueError
            return num_questions
        except ValueError:
            print("Invalid choice. Please enter a valid number (10, 25, 50, 100).")

# Function to handle the game logic
def handle_game(words, sentences, questionWords):
    while True:
        print("Choose the game you want to play:")
        print("1. Word Quiz")
        print("2. Question Maker Game")
        print("3. Question words practicing")
        game_choice = input("Enter 1, 2 or 3: ").strip()

        if game_choice == '1':
            num_questions = get_num_questions()
            print("Translate the following German words into English!")
            quiz_user(words, num_questions)

        elif game_choice == '2':
            num_questions = get_num_questions()
            print("Convert the following declarative sentences into question form!")
            question_maker(sentences, num_questions)

        elif game_choice == '3':
            num_questions=get_num_questions()
            print('Try to guess the question words of the sentences!')
            words_of_question(questionWords, num_questions)
        else:
            print("Invalid choice. Please enter 1 or 2.")
            continue

        while True:
            restart_choice = input("Press 'X' to exit or 'S' to start again: ").strip().upper()
            if restart_choice == 'X':
                print("Goodbye!")
                return
            elif restart_choice == 'S':
                break
            else:
                print("Invalid choice. Please press 'X' to exit or 'S' to start again.")

# Main function to load data and start the game
def main():
    words_file = 'beginner_german_words.csv'
    sentences_file = 'german_sentences.csv'
    words_of_question_file = 'question_words.csv'
    words = load_words(words_file)
    sentences = load_sentences(sentences_file)
    questionWords = load_questions(words_of_question_file)

    print("Welcome to the German Learning Game!")
    handle_game(words, sentences, questionWords)

if __name__ == "__main__":
    main()