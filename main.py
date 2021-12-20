############### Blackjack Project
import random
import art
from replit import clear

user_cards = []
user_total = 0
computer_cards = []
computer_total = 0
game_start = False
play_game = input("Do you want to play a game of Blackjack? y/n: ")


def deal_card(num):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    drawn_card = []
    for card in range(num):
        drawn_card.append(random.choice(cards))
    return drawn_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_total, computer_total):
    if user_total > 21 and computer_total > 21:
        return "You went over. You lose 😤"
    elif user_total == computer_total:
        return "Draw 🙃"
    elif computer_total == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_total == 0:
        return "Win with a Blackjack 😎"
    elif user_total > 21:
        return "You went over. You lose 😭"
    elif computer_total > 21:
        return "Opponent went over. You win 😁"
    elif user_total > computer_total:
        return "You win 😃"
    else:
        return "You lose 😤"


def game():
    game_start = True

    print(art.logo)

    user_cards = deal_card(2)
    computer_cards = deal_card(2)

    while game_start == True:
        user_total = calculate_score(user_cards)
        computer_total = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}")
        print(f"Total: {user_total}")
        print(f"Dealer's Hand: {computer_cards[0]}")

        if user_total == 0 or computer_total == 0 or user_total > 21:
            game_start = False
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards += deal_card(1)
            else:
                game_start = False

    while computer_total != 0 and computer_total < 17:
        computer_cards += deal_card(1)
        computer_total = calculate_score(computer_cards)
           
    print(compare(user_total, computer_total))
    print(f"Your cards: {user_cards} and total: {user_total}")
    print(f"Dealer's cards: {computer_cards} and total: {computer_total}")

    if input("Do you want to play another round? y/n: ") == 'y':
        game_start = True
        clear()
        game()

    else:
        game_start = False


if play_game == 'y':
    game()

