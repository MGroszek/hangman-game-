# Hangman Game

import random


def get_random_word():
    words = ['python', 'java', 'kotlin', 'javascript']
    return random.choice(words)


def ask_play_again():
    response = input("Do you want to play again? (y/n): ").lower().strip()
    return response.startswith('y')  # check if the response starts with 'y'


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,
        # head, torso, both arms, and one leg
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     /
           -
        """,
        # head, torso, and both arms
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |
           -
        """,
        # head, torso, and one arm
        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |
           -
        """,
        # head and torso
        """
           --------
           |      |
           |      O
           |      |
           |      |
           |
           -
        """,
        # head
        """
           --------
           |      |
           |      O
           |
           |
           |
           -
        """,
        # initial empty state
        """
           --------
           |      |
           |
           |
           |
           |
           -
        """
    ]
    return stages[tries]


def play_hangman():
    word = get_random_word()
    word_completion = '_' * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print("Let's play Hangman!")
    print(display_hangman(tries))
    print(f"Tries left: {tries}")
    print(word_completion)
    print()
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already guessed the letter", guess)
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                for i, letter in enumerate(word):
                    if letter == guess:
                        word_as_list[i] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("You already guessed the word", guess)
            elif guess != word:
                print(guess, "is not the word.")
                tries -= 1
                guessed_words.append(guess)
            else:
                word_completion = word
                guessed = True
        else:
            print("Invalid input. Please try again.")

        print(display_hangman(tries))
        print(f"Tries left: {tries}")
        print(word_completion)
        print()

    if guessed:
        print("Congratulations, you guessed the word! You win!")
    else:
        print("Sorry, you ran out of tries. The word was " + word +
              ". Maybe next time!")


if __name__ == "__main__":
    while True:
        play_hangman()
        if not ask_play_again():
            print("Thanks for playing!")
            break
