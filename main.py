from random import choice
import os

# Array to hold cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10,
         10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
shuffled_cards = cards.copy()
total_chips = int(input("How much would you like to start with today?\n"))
bet = 0
# Function that will shuffle cards when the number of cards is less than 10


# Function that will add a card from shuffled_cards to a player/dealer's hand and remove it from the array


def deal_card():
    dealt_card = choice(shuffled_cards)
    shuffled_cards.remove(dealt_card)
    return dealt_card

# Remove any face cards or aces


# def normalize(card_list):
#     if "A" in card_list:
#         card_list.remove("A")
#         card_list.append(11)
#     elif "J" in card_list:
#         card_list.remove("J")
#         card_list.append(10)
#     if "Q" in card_list:
#         card_list.remove("Q")
#         card_list.append(10)
#     if "K" in card_list:
#         card_list.remove("K")
#         card_list.append(10)


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
        return "You lose, dealer has Blackjack!"
        game_over = True
    elif user_score == 0:
        return "You win, you got blackjack!"
        game_over = True
    elif user_score > 21:
        return "You busted, you lose."
        game_over = True
    elif computer_score > 21:
        return "You win! The dealer busted."
        game_over = True
    elif user_score > computer_score:
        return "You win!"
        game_over = True
    else:
        return f"You lose, the dealer had {computer_score}"
        game_over = True


# Change bet to reward a win or keep the bet on a loss


# Main game function


def game():
    global total_chips
    if total_chips <= 0:
        print("You are out of money, come back with more!")
        exit()
    bet = int(input("How much would you like to bet this hand?\n"))
    total_chips -= bet
    print("Taking bets now...")
    user_cards = []
    computer_cards = []
    print("Dealing cards now...")
    # print(shuffled_cards)
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    print(f"Your cards: {user_cards}")
    print(f"The dealer's up card is {computer_cards[0]}")
    # normalize(user_cards)
    # normalize(computer_cards)
    while not game_over:

        user_score = calculate_score(user_cards)
        if user_score == 21 and len(user_cards) == 2:
            game_over = True
            print("Blackjack! You win!")
        computer_score = calculate_score(computer_cards)

        if computer_score == 0 or user_score == 21 or user_score > 21:
            game_over = True
        else:
            choice = input(
                "Would you like to 'hit', 'split', 'double', or 'stay'?\n")
            if choice == 'hit':
                user_cards.append(deal_card())
                print(user_cards)
            elif choice == 'split':

                if user_cards[0] == user_cards[1]:
                    second_hand = user_cards[1]
                    user_cards.remove(user_cards[1])
                    user_cards.append(deal_card())
                    second_hand.append(deal_card())
            elif choice == 'double':
                # TODO: ADD BETTING, AND THEN THE OPTION FOR A PLAYER TO DOUBLE DOWN ON THEIR HAND, LIMITING THEM TO ONE CARD
                user_cards.append(deal_card())
                game_over = True
            elif choice == 'stay':
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your hand was {user_cards}")
    print(f"The computer's hand was {computer_cards}")
    print(compare(user_score, computer_score))
    # print(f"Total chips: {total_chips}")
    # Change bet to reward a win or keep the bet on a loss

    if computer_score == user_score:
        bet = bet
    elif computer_score == 0:
        bet = 0
    elif user_score == 0:
        bet *= 2.5
    elif user_score > 21:
        bet = 0
    elif computer_score > 21:
        bet *= 2
    elif user_score > computer_score:
        bet *= 2
    else:
        bet = 0

    # print(bet)
    total_chips += bet
    print(f"Total chips: {total_chips}")


print("Welcome to Blackjack Practice!")
game()
keep_playing = True
while keep_playing:
    if input("Would you like to play another hand? Type 'y' for yes, 'n' for no.\n") == 'y':
        os.system('cls')
        if len(shuffled_cards) < 10:
            print("Shuffling now")
            shuffled_cards = cards.copy()
        game()
    else:
        exit()
