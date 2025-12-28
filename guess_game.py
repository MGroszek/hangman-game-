# Guess the Number Game
import random  # Importing random module to generate random numbers


def guess_number():
    number = random.randint(1, 100)  # Random number between 1 and 100
    attempts = 0
    print("Welcome to the Guess the Number Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1  # Increment attempt count

            if user_guess < number:
                print("Too low! Try again.")
            elif user_guess > number:
                print("Too high! Try again.")
            else:
                print(
                    f"Congratulations! You've guessed the number {number} in {attempts} attempts.")
                break
            if attempts >= 5:  # Limit attempts to 5
                print(
                    f"Sorry, you've used all your attempts. The number was {number}.")
                break
        except ValueError:  # Handle non-integer inputs
            print("Please enter a valid integer.")


guess_number()
