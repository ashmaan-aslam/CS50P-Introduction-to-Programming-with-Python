import pyfiglet
import random
import sys

# Initialize the Figlet object
figlet = pyfiglet.Figlet()

# Argument handling
if len(sys.argv) == 1:
    # No arguments, use a random font
    font = random.choice(figlet.getFonts())
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    # Two arguments provided, validate the font
    font = sys.argv[2]
    if font not in figlet.getFonts():
        sys.exit("Error: Invalid font name!")
else:
    # Invalid arguments
    sys.exit("Usage: figlet.py [-f FONT]")

# set the chosen font
figlet.setFont(font=font)

# prompt the user for input
user_input = input("Input: ")

# render and display the ASCII art
print(figlet.renderText(user_input))
