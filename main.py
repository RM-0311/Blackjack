import random
import os

# Array to hold cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

# Function that will add a card to a player/dealer's hand


def deal_card():
    return random.choice(cards)

# Calculate the score of the given hand


def calculate_score(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    elif sum(card_list) > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        return sum(card_list)
    else:
        return sum(card_list)

# Compare the scores of the two hands given and reach a conclusion


def compare(user_score, computer_score):
    if computer_score == user_score:
        return "Draw"
        game_over = True
    elif computer_score == 0:
        return "You lose, computer has Blackjack!"
        game_over = True
    elif user_score == 0:
        return "You win, you got blackjack!"
        game_over = True
    elif user_score > 21:
        return "You busted, you lose."
        game_over = True
    elif computer_score > 21:
        return "You win! The computer busted."
        game_over = True
    elif user_score > computer_score:
        return "You win!"
        game_over = True
    else:
        return "You lose"
        game_over = True

# Main game function


def game():
    user_cards = []
    computer_cards = []
    print("Dealing cards now...")
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}")
        if computer_score == 0 or user_score == 21 or user_score > 21:
            game_over = True
        else:
            hit = input(
                "Would you like another card? Type 'y' for yes and 'n' for no'.")
            if hit == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your hand was {user_cards}")
    print(f"The computer's hand was {computer_cards}")
    print(compare(user_score, computer_score))


print("Welcome to Blackjack!")
game()
if input("Would you like to restart the game? Type 'y' for yes, 'n' for no.") == 'y':
    os.system('cls')
    game()
else:
    exit()
