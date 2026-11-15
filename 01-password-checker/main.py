# Basic Password Checker
# Coded by Rak0ne
# 11/15/2026
# Finished in 2h30 (6:33 PM)

# Imports
import os
import time
import sys
# Vars
PW = 123321
isdebug = False
hint = "123 by 321"
max_tries = 3

# Pyfiglet
try:
    import pyfiglet
except ModuleNotFoundError:
    print("Pyfiglet not found. Do you want to install?\n1. Yes\n2. No")
    try:
        askpy = int(input(">> "))
        if askpy == 1:
            os.system("pip install pyfiglet")
            print("Installed! Please execute again.")
            time.sleep(3)
            sys.exit(0)
        elif askpy == 2:
            print("Quitting...")
            sys.exit(0)
        else:
            print("Invalid choice!")
            sys.exit(1)
    except ValueError:
        print("Only numbers are allowed.")
        sys.exit(1)

# Defs
def debug(text):
    if isdebug == True:
        print(text)

def check(tries):
    if tries <= 0:
        print("You have exceeded the maximum of 3 attempts. Please try again.")
        return False
    return True

def choices():
    print("")
    os.system("pyfiglet -c WHITE Rak0ne")
    print("Basic Password Checker v1.0")
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

def main():
    os.system("clear")
    tries = max_tries
    canhint = True
    print("Hello, Please type your password to log-in.")
    while check(tries):
        try:
            ask = input(">> ")
            if ask == str(PW):
                choices()
            elif len(ask) <= 2:
                if ask == "1":
                    if canhint == True:
                        print(hint)
                        canhint = False
                    else:
                        print("You can't ask for hint twice.")
                else:
                    print("It needs at least 3 digits, with no negative numbers or special characters.")
            else:
                tries -= 1;
                if tries >= 1:
                    print(f"Wrong Password! Please try again. {tries} Tries left.")
                else:
                    print("Wrong Password! Please try again.")
                if canhint == True:
                    if tries >= 1:
                        print("You have a hint left. Type 1 if you want to see it.")

        except ValueError:
            print("Only numbers are allowed.")

# Main

if __name__ == "__main__":
    main()
