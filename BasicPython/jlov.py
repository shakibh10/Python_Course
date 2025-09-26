from colorama import Fore, Style, init
from pyfiglet import Figlet
import time
import os

# Initialize colorama
init()

# Function to display a colorful animated heart
def print_heart():
    heart = [
        "       *****       *****       ",
        "     *********   *********     ",
        "   ************* ************* ",
        "  ***************************** ",
        "   ***************************  ",
        "     ***********************    ",
        "       *******************      ",
        "         ***************        ",
        "           ***********          ",
        "             *******            ",
        "               ***              ",
        "                *               ",
    ]

    for line in heart:
        print(Fore.RED + line.center(80))
        time.sleep(0.1)
    print(Style.RESET_ALL)

# Function to display the message in an artistic font and color
def print_message():
    fig = Figlet(font='slant')
    message = "I Love You, Jui"
    styled_message = Fore.MAGENTA + Style.BRIGHT + fig.renderText(message)
    print(styled_message)
    print(Style.RESET_ALL)

# Function to add sparkle effects
def sparkle_effect():
    sparkles = ["✨", "💖", "🌟", "💕", "💫"]
    for _ in range(10):
        print(" ".join(Fore.YELLOW + sparkles[_ % len(sparkles)] for _ in range(30)).center(80))
        time.sleep(0.2)
    print(Style.RESET_ALL)

if __name__ == "__main__":
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the screen
    sparkle_effect()
    print_heart()
    time.sleep(0.5)
    print_message()
    sparkle_effect()
