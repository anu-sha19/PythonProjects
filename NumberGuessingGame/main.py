import random

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_guess(actual_number, guess):
    difference = actual_number - guess
    abs_diff = abs(difference)

    hint = "higher" if difference > 0 else "lower"

    if difference == 0:
        print("Yay! you guessed the number!")
        return True

    if abs_diff <= 5:
        print(f"Almost there. Try {hint}!")

    elif abs_diff >= 20:
        print(f"Guess too far off! Try {hint}!")
    else:
        print(f"You're getting there. But, try {hint}")
    print()


def set_difficulty():
    level = input("Choose the difficulty level. 'e' for Easy and 'h' for Hard: ")
    attempts = EASY_LEVEL_TURNS
    if level == 'h':
        attempts = HARD_LEVEL_TURNS
    return attempts


def game():
    number = random.randint(0, 101)
    print(number)
    attempts = set_difficulty()

    while True:
        print(f"You have {attempts} attempts remaining.")
        if attempts == 0:
            print(f"Game Over! The correct number is {number}!")
            break

        guess = int(input("Take a guess between 1-100: "))
        if check_guess(number, guess):
            break
        else:
            attempts -= 1


game()
