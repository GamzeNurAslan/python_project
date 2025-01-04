from random import randint
from art import logo
from imza import imza

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def check_answer(user,computer,turns):
    if user > computer:
        print("Too high")
        return turns - 1
    elif user < computer:
        print("Too low")
        return turns - 1
    else:
        print(f"You got it! The answer was {computer}")

def chose_difficulty():
    level = input("Choose a difficulty.Type 'easy' or 'hard : ").lower()
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
     print(logo)
     print("Welcome to the Number Guessing Game!")
     print("I'm thinking of a number between 1 and 100: \n")
     answer = randint(1, 100)

     turns = chose_difficulty()

     guess = 0
     while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")

     print(f"Congratulations! You've guessed the correct number {answer}")
     print(imza)


game()
