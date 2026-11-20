# Coded by Rak0ne
# 6:38 PM - 8:01 PM
# ROCK PAPER SCISSOR SHOOT GAME
# It took me this long because I had to have dinner... and I take a long time. a long, time...
# Imports
import sys
import random
import time
import os

# Settings
isdebug = False
# Clear
os.system("clear")

# Functions
def generate_cpu_choice():
    return random.randint(1, 3)

def won():
    os.system("clear")
    os.system("pyfiglet -c WHITE Rak0ne")
    print("Basic Rock Paper Scissors Game v1.0")
    print("")
    print("1. Rak0ne Github\n2. Uninstall Pyfiglet")
    try:
        choice = int(input(">> "))
        if choice == 1:
            print("https://github.com/Rak0ne")
            sys.exit(0)
        elif choice == 2:
            os.system("pip uninstall pyfiglet -y")
            print("Uninstalled successfully. Quitting...")
            sys.exit(0)
        else:
            print("Invalid choice!")
            sys.exit(1)
    except ValueError:
        print("Only numbers are allowed.")
        sys.exit(1)

def game():
    cpu_points = 0
    user_points = 0
    try:
        while True:
            if cpu_points == 3:
                print("CPU wins the game!")
                print(f"Results:\nCPU: {cpu_points}\nUSER: {user_points}")
                sys.exit(0)
            elif user_points == 3:
                print("User wins the game!")
                print(f"Results:\nCPU: {cpu_points}\nUSER: {user_points}")
                time.sleep(3)
                won()
                break

            cpuchoice = generate_cpu_choice()
            print("---> POINTS <---")
            print(f"YOU: {user_points}\nCPU: {cpu_points}")
            print("")
            print("Rock...")
            time.sleep(0.5)
            print("Paper...")
            time.sleep(0.5)
            print("Scissors...")
            time.sleep(1)
            print("Shoot!")
            debug(f"CPU choice: {cpuchoice}")
            choice = str(input(">> ")).lower()

            if choice == "r" or choice == "rock":
                if cpuchoice == 1:
                    print("You chose: Rock\nCPU chose: Rock")
                    time.sleep(1.5)
                    print("It's a draw!")
                    time.sleep(1.5)
                    os.system("clear")
                elif cpuchoice == 2:
                    print("You chose: Rock\nCPU chose: Paper")
                    time.sleep(1.5)
                    print("CPU Wins!")
                    cpu_points += 1
                    time.sleep(1.5)
                    os.system("clear")
                elif cpuchoice == 3:
                    print("You chose: Rock\nCPU chose: Scissors")
                    time.sleep(1.5)
                    print("You Win!")
                    user_points += 1
                    time.sleep(1.5)
                    os.system("clear")

            elif choice == "p" or choice == "paper":
                if cpuchoice == 1:
                    print("You chose: Paper\nCPU chose: Rock")
                    time.sleep(1.5)
                    print("You Win!")
                    user_points += 1
                    time.sleep(1.5)
                    os.system("clear")
                elif cpuchoice == 2:
                    print("You chose: Paper\nCPU chose: Paper")
                    time.sleep(1.5)
                    print("It's a draw!")
                    time.sleep(1.5)
                    os.system("clear")
                elif cpuchoice == 3:
                    print("You chose: Paper\nCPU chose: Scissors")
                    time.sleep(1.5)
                    print("CPU Wins!")
                    cpu_points += 1
                    time.sleep(1.5)
                    os.system("clear")

            elif choice == "s" or choice == "scissors":
                if cpuchoice == 1:
                    print("You chose: Scissors\nCPU chose: Rock")
                    time.sleep(1.5)
                    print("CPU Wins!")
                    cpu_points += 1
                    time.sleep(1.5)
                    os.system("clear")
                elif cpuchoice == 2:
                    print("You chose: Scissors\nCPU chose: Paper")
                    time.sleep(1.5)
                    print("You Win!")
                    user_points += 1
                    time.sleep(1.5)
                    os.system("clear")
                elif cpuchoice == 3:
                    print("You chose: Scissors\nCPU chose: Scissors")
                    time.sleep(1.5)
                    print("It's a draw!")
                    time.sleep(1.5)
                    os.system("clear")

    except KeyboardInterrupt:
        print("Thanks for playing! bye.")
        sys.exit(0)

def main():
    os.system("clear")
    game()

# Debug
def debug(msg):
    if isdebug == True:
        print(msg)

# Pyfiglet
try:
    import pyfiglet
except ModuleNotFoundError:
    while True:
        print("Pyfiglet not found. install?\n1. Yes\n2. No")
        try:
            pyfiglet_ask = int(input(">> "))
            if pyfiglet_ask == 1:
                print("installing...")
                os.system("pip install pyfiglet")
                print("Installed! Continuing...")
                time.sleep(3)
                main()
                break

            elif pyfiglet_ask == 2:
                print("You chose to cancel. Quitting...")
                sys.exit(0)

            else:
                os.system("clear")
                print("Invalid input! Use 1 to Install and 2 to Cancel.")

        except ValueError:
            os.system("clear")
            print("Invalid input! Use 1 to Install and 2 to Cancel.")

if __name__ == "__main__":
    main()
