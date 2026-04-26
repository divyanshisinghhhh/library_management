from roll_dice import dice
from stone_paper_scissor import sps

def game():
    while True:
        print("------- LET'S PLAY A GAME -------")
        print("\n 1. Stone, Paper, Scissor Game")
        print("2. Dice Roll Game")
        print("3. Exit")
        choice = int(input("Please enter the game you want to play: "))
        if choice == 1:
            sps()
        elif choice == 2:
            dice()
        elif choice == 3:
            print("THANK YOU !!! YOU ARE LEAVING OUR PLAYSTATION")
            break
        else:
            print("invalid choice")

game()