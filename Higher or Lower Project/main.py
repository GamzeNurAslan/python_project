import random
from art import logo
from art import vs
from game_data_2 import data

def format_data(account):
    account_name = account["name"]
    account_descrp = account["description"]
    account_capital_city = account["capital_city"]
    return f"{account_name} , {account_descrp} , {account_capital_city}"

def check_answer(user_guess,a_followers,b_followers):
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)

while game_should_continue:

    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    print("\n" * 20)
    print(logo)


    a_follower_count = account_a["population"]
    b_follower_count = account_b["population"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print(f"You're right! Current score {score}")
    else:
        print(f"Sorry, that's wrong. Final score: {score}.")
        game_should_continue = False
