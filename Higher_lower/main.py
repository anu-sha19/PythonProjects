from game_data import data
from art import logo, vs
import random
import time

"""
Higher Lower Game

Guess who has more Instagram followers between two public figures.
Each correct guess increases your score. The game ends when you guess wrong.
Data comes from `game_data`, and visuals from `art`.
"""
def get_stats(label, index):
    person = data[index]
    print(f"Compare {label}: {person['name']}, a {person['description']}, from {person['country']}")
    return index

def check_answer(chosen_person, other):

    return chosen_person['follower_count'] > other['follower_count']


def higher_lower():
    print(logo)
    score = 0
    num = len(data)

    a_index = random.randint(0, num-1) # random index to get a random person from the data
    person_A = get_stats('A', a_index)

    while True:
        print(vs)

        b_index = random.randint(0,num-1)

        while a_index == b_index: # make sure you are not comparing the same person
            b_index = random.randint(0, num)

        person_B = get_stats('B', b_index)

        answer = (input("Who has more followers. Type A or B:")).lower()

        chosen_person = data[person_A if answer == 'a' else  person_B]
        other_person = data[person_B if answer == 'a' else person_A]

        if check_answer(chosen_person, other_person ):
            score += 1
            print(f"You are right! Current score: {score}")
            time.sleep(1)

            print('\n' * 100)

            print(logo)

            person_A = get_stats('A', person_A if answer == 'a' else  person_B)

        else:
            print(f"Sorry that's wrong. Final score: {score}")
            play_again = (input("Would you like to play another game of higher lower? Type 'y' or 'n:")).lower()
            if play_again == 'y':
                print('\n' * 100)
                higher_lower()

            return

higher_lower()