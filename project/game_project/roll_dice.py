import random

def dice():
    user_roll = random.randint(1,6)
    computer_roll = random.randint(1,6)

    print(f"you rolled: {user_roll}")
    print(f"computer rolled: {computer_roll}")

    if user_roll > computer_roll:
        print("Congratulations!! you wins the game")
    elif computer_roll > user_roll:
        print("OOP'S !!! you lost")
    else:
        print("it is a draw!! try again next time")