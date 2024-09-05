import random

def get_random_word():
    # List of words to choose from
    words = ["python", "hangman", "artificial", "intelligence", "university", "programming"]
    return random.choice(words)

def display_hangman(tries):
    stages = [
                """
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  / \\
                   |
                """,
                """
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  / 
                   |
                """,
                """
                   -----
                   |   |
                   |   O
                   |  /|\\
                   |  
                   |
                """,
                """
                   -----
                   |   |
                   |   O
                   |  /|
                   |  
                   |
                """,
                """
                   -----
                   |   |
                   |   O
                   |   |
                   |  
                   |
                """,
                """
                   -----
                   |   |
                   |   O
                   |  
                   |  
                   |
                """,
                """
                   -----
                   |   |
                   |   
                   |  
                   |  
                   |
                """
    ]
    return stages[tries]

def play_hangman():
    word = get_random_word()
    word_display = "_" * len(word)
    guessed = False
    guessed_letters = []
    tries = 6

    print("Welcome to Hangman!")
    print(display_hangman(tries))
    print("Word: ", word_display)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Please guess a letter: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter:", guess)
            elif guess not in word:
                print("Wrong guess:", guess)
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good guess:", guess)
                guessed_letters.append(guess)
                word_as_list = list(word_display)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_display = "".join(word_as_list)

                if "_" not in word_display:
                    guessed = True
        else:
            print("Invalid input. Please enter a single letter.")

        print(display_hangman(tries))
        print("Word: ", word_display)
        print("\n")

    if guessed:
        print("Congratulations! You guessed the word:", word)
    else:
        print("Sorry, you ran out of tries. The word was:", word)

if __name__ == "__main__":
    play_hangman()
