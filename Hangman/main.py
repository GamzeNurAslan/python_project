import random
from hangman_words import word_list
from hangman_art import stages

stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = r''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''


word_list = ["lemon", "strawberry", "blackberry", "jam", "pen", "rain", "keyboard", "mouse", "computer", "engineer",
             "polarbear", "koala", "sloth", "camel"]

lives = 6
chose_word = random.choice(word_list)  # Randomly choose a word from the list
placeholder = "_" * len(chose_word)  # Create a string of underscores to represent the word
word_length = len(chose_word)

print(placeholder)

game_over = False
correct_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()

    print(f"****************************{lives}/6 LIVES LEFT****************************")

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    if guess in chose_word:
        correct_letters.append(guess)
        print("Right!")
    else:
        lives -= 1
        print("Wrong!")

    display = ""
    for letter in chose_word:
        if letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)

    print(stages[lives])

    if "_" not in display:
        game_over = True
        print("You win!")
        print(logo)

    if lives == 0:
        game_over = True
        print(f"***********************IT WAS {chose_word}! YOU LOSE**********************")
        print(logo)
