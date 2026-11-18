# Coded by Rak0ne
# 6:06 PM - 6:59 PM
# Basic Guess The Number Game
# I was going to add attempts, but I got lazy, so it's left as is.

# Imports
import time
import os
import random
import sys
os.system("clear")

# VARs
isdebug = True

try:
    import pyfiglet
except ModuleNotFoundError:
    print("pyfiglet not found. install?\n0. - Cancel\n1. - Install")
    while True:
        try:
            askpy = int(input(">> "))
            if askpy > 1:
                print("too high")
            elif askpy < 0:
                print("too low")
            else:
                if askpy == 1:
                    os.system("pip install pyfiglet")
                    print("pyfiglet is installed. starting")
                    time.sleep(2.5)
                    os.system("clear")
                    break
                elif askpy == 0:
                    print("Quitting...")
                    sys.exit(0)
        except ValueError:
            print("Impossible value! 0 to cancel, 1 to install.")

# Number
def newnumber():
    return random.randint(0, 100)

# Debug
def debug(text):
    if isdebug == True:
        print(text)

# Menu
def menu():
    os.system("clear")
    os.system("pyfiglet -c WHITE Rak0ne")
    print("Basic Guess the Number game v1.0")
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

# Win
def win():
    print("You guessed the correct number!")
    time.sleep(1.5)
    print(f"The number was: {number}")
    time.sleep(2)
    print("Play Again? Y/N")
    while True:
        askplag = str(input(">> ")).upper()
        if askplag == "Y":
            os.system("clear")
            main()
            break
        elif askplag == "N":
            menu()
            break
        else:
            print("Invalid call! Use Y for yes, N for no.")

# Main
def main():
    global number
    number = newnumber()

    print("Enter Your Guess:\n")
    debug(f"Number: {number}")
    while True:
        try:
            ask = int(input(">> "))
            if ask > 100:
                print("That's a very high value. Try a number below 101.")
                time.sleep(0.5)
            elif ask < 0:
                print("This value is too low. Try a value above -1.")
                time.sleep(0.5)
            else:
                if ask == number:
                    win()
                    break
                elif ask > number:
                    print("Too high! Try lower.")
                elif ask < number:
                    print("Too low! Try higher.")
        except ValueError:
            print("Impossible value! Try from 0 to 100 without special characters.")
            time.sleep(0.5)

if __name__ == "__main__":
    main()
