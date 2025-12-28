# Paper,Scissors,Rock Game
import random


def get_user_choice():
    choices = ['paper', 'scissors', 'rock']
    user_choice = input("Enter your choice (Paper, Scissors, Rock): ").lower()
    while True:
        if user_choice in choices:
            return user_choice
        else:
            user_choice = input(
                "Invalid choice. Please enter Paper, Scissors, or Rock: ").lower()


def get_computer_choice():
    choices = ['paper', 'scissors', 'rock']
    return random.choice(choices)


def winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'rock' and computer_choice == 'scissors'):
        return "You win!"
    else:
        return "You lose!"


def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    print(winner(user_choice, computer_choice))


play_game()
