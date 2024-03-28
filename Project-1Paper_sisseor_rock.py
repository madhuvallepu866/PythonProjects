import random
user_choice=int((input("Enter Your choice: Type 0 for Rock, 1 for paper,2 for scissors:")))
if user_choice >= 3 or user_choice < 0 :
    print("You entered Invalid Num and  You lose")
else:
    computer_choice=random.randint(0,2)
    print("Computer Choice:")
    print(computer_choice)
    if computer_choice == user_choice:
        print("Its a draw game")
    elif computer_choice == 0 and user_choice == 2:
        print("You Lose")
    elif user_choice == 0 and computer_choice == 2:
        print("You win")
    elif computer_choice > user_choice:
        print("You Lose.")
    elif user_choice > computer_choice:
        print("You win.")
