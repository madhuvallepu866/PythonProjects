import random
import Textkool_art_log
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen == 'easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen == 'hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return

def check_answer(guessed_number,answer,attempts):
    if guessed_number < answer:
        print("Your Guess is too low")
        return attempts-1
    elif guessed_number > answer:
        print("Your guess is too High")
        return attempts-1
    else:
        print(f"Your Guess is right... The answer was {answer}")
def guess_game():
    print(Textkool_art_log.logo)
    print("Let me think of a number between 1 to 50.")
    answer=random.randint(1,50)
    #print(answer)
    level=input("Choose lavel Of Difficulty.... Type 'easy' OR 'hard': ").lower()
    attempts=set_difficulty(level)
    if attempts!= EASY_LEVEL_ATTEMPTS and attempts!= HARD_LEVEL_ATTEMPTS:
        print("Your choosed Wrong Lavel Choose Correct One and play again")
        return
    guessed_number=0
    while guessed_number != answer :
        print(f"You have {attempts} remaining to guess the number.")
        guessed_number=int(input("Guess the number: "))
        attempts=check_answer(guessed_number,answer,attempts)
        if attempts == 0:
            print("Your out of Guesses... You Lose!!")
            return
        elif guessed_number != answer:
            print("Guess again")
guess_game()