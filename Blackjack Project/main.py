import random
import art
from art import logo
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(b_score, k_score):
    if b_score == k_score:
        return "Draw 🙃"
    elif k_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif b_score == 0:
        return "Win with a Blackjack 😎"
    elif b_score > 21:
        return "You went over. You lose 😭"
    elif k_score > 21:
        return "Opponent went over. You win 😁"
    elif b_score > k_score:
        return "You win 😃"
    else:
        return "You lose 😤"


def play_game():
    print(logo)
    b_cards = []
    k_cards = []
    k_score = -1
    b_score = -1
    is_game_over = False

    for _ in range(2):
        b_cards.append(deal_card())
        k_cards.append(deal_card())


    while not is_game_over:
        b_score = calculate_score(b_cards)
        k_score = calculate_score(k_cards)
        print(f"Your cards {b_cards},current score {b_score}")
        print(f"The other person's first card: {k_cards[0]}")

        if b_score == 0 or k_score == 0 or b_score > 21:
           is_game_over = True

        else:
            b_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if b_should_deal == "y":
                 b_cards.append(deal_card())
            else:
                is_game_over = True


    while k_score != 0 and k_score < 17:
            k_cards.append(deal_card())
            k_score = calculate_score(k_cards)

    print(f"Your final hand: {b_cards}, final score: {b_score}")
    print(f"Computer's final hand: {k_cards}, final score: {k_score}")
    print(compare(b_score, k_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") ==  "y":
    print("\n" * 50)
    play_game()


