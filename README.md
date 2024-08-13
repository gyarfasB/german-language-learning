# German language learning game
## written in python by me and openAI

The program includes 3 small games:

1. Word Quiz
2. Question Maker Game
3. Question words practicing

You can choose the number of test items (10,25,50 or 100). I filter the user input, so you can only enter valid numbers.
Like this: 

`def get_num_questions():
    while True:
        print("Choose the number of items for the game: 10, 25, 50, 100")
        try:
            num_questions = int(input("Enter the number of questions: "))
            if num_questions not in [10, 25, 50, 100]:
                raise ValueError
            return num_questions
        except ValueError:
            print("Invalid choice. Please enter a valid number (10, 25, 50, 100).")`

Operation: 

Run the **main.py** file, to play.
The program reads different CSV files to load the words/sentences:

"beginner_german_words.csv" (head: German,English)
"german_sentences.csv" (head: Declarative,Question)
"question words.csv" (head: Question Sentence,Missing word)

You can replace the .csv files to **use your own words**, but you should take care of the **head** of the files, if you don't want to change any code.

After you complete the test, you'll see the final results. Then press '**X**' to exit, and press '**S**' to start again.


