from colorama import Fore, Style, init
import time
import os

# Initialize colorama
init()

def print_heart():
    heart = [
        "  ***     ***  ",
        " *****   ***** ",
        "******* *******",
        " ************* ",
        "  ***********  ",
        "   *********   ",
        "    *******    ",
        "     *****     ",
        "      ***      ",
        "       *       ",
    ]

    for line in heart:
        print(Fore.RED + line.center(50))
        time.sleep(0.2)

def print_message():
    message = "I Love You, Jui"
    styled_message = Fore.MAGENTA + Style.BRIGHT + message.center(50)
    print(styled_message)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    print_heart()
    time.sleep(0.5)
    print_message()