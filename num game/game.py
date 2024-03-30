import random

EASY_LEVEL_ATTEMPTS = 10
HARD_LEVEL_ATTEMPTS = 5

def set_difficulty(level_chosen):
    while level_chosen not in ['easy', 'hard']:
        print("Invalid input. Please choose either 'easy' or 'hard'.")
        level_chosen = input("Choose level of difficulty...Type 'easy' or 'hard': ")
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    else:
        return HARD_LEVEL_ATTEMPTS

def check_answer(guessed_number, answer, attempts):
    if guessed_number < answer:
        print("Your guess is too low")
        print("Guess again")
        return attempts - 1
    elif guessed_number > answer:
        print("Your guess is too high")
        print("Guess again")
        return attempts - 1
    else:
        print(f"Your guess is correct.... The answer was {answer}")
        return 0

def game():
    print("Let me think of a number between 1 to 200")
    answer = random.randint(1, 200)
    level = input("Choose level of difficulty...Type 'easy' or 'hard': ")
    attempts = set_difficulty(level)
    guessed_number = 0
    while guessed_number != answer:
        print(f"You have {attempts} attempts remaining.")
        guessed_number = int(input("Guess a number: "))
        attempts = check_answer(guessed_number, answer, attempts)
        if attempts == 0:
            print("You are out of guesses")
            return

game()
