#blackjack

# 1) Ask the user if they want to play the game
#2) Show them 2 random cards for the player  AND one random card of the computer but computer has drawn 2 , we only show one
# 3) ask the user if they want to get another card
# 4) if ans is yes: draw another random card from the list
#  proceed to count the total value of the cards against two players
# if the total value is less than 21 for both, whoeveer has the highest value wins
# if its over 21, whoever has the lowest value wins
# if one is over 21 and the other is below, the one who has lesser value wins
# if both have a 21 , its a draw

import random

def deal_card():
    '''returns a random card from the deck'''
    deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(deck)
    return card



def game_rules(player_cards, comp_cards):
    p_score = sum(player_cards)
    c_score = sum(comp_cards)

    if p_score > 21:
        return -1
    if p_score == c_score:
        return 0
    if p_score == 21:
        return 1
    if c_score > 21:
        return 1
    if p_score < 21 and p_score > c_score:
        return 1
    else:
        return -1


def final_message(player_cards, comp_cards):
    print(f"Your final hand: {player_cards}, final score: {sum(player_cards)}")
    print(f"Computer's final hand: {comp_cards}, final score: {sum(comp_cards)}")


def game_play():
    play = input("Would you like to play the game of blackjack? Type 'y or 'n: ")
    if play == 'n':
        return
    print("\n" * 100)
    player_cards = []
    comp_cards = []

    for _ in range(2):
        player_cards.append(deal_card())
        comp_cards.append(deal_card())

    while True:

        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {comp_cards[0]}")

        if sum(player_cards) > 21:
            final_message(player_cards, comp_cards)
            print("You went over! You lose")
            break

        another_draw = (input("Type 'y' to get another card, type 'n' to pass: ").lower())
        if another_draw == 'y':
            new_card = deal_card()
            if new_card == 11:
                if new_card + sum(player_cards) > 21:
                    new_card = 1
            player_cards.append(new_card)

            if sum(player_cards) > 21:
                final_message(player_cards, comp_cards)
                print("You went over! You lose")
                break

        elif another_draw == 'n':
            while sum(comp_cards) < 17:
                comp_cards.append(deal_card())

            result = game_rules(player_cards, comp_cards)

            final_message(player_cards, comp_cards)

            if result == 0:
                print("Draw!")

            elif result == 1:
                print("You won!")

            else:
                print("You lose!")
            break
    game_play()


game_play()
