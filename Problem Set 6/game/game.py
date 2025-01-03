import random

while True:
    try:
        level = int(input("Level: "))  # Ask for integer n
        if level <= 0:  # Ensure level is positive
            continue
        random_integer = random.randint(1, level)  # Generate random number from 1 to n
        break  # Exit the loop once a valid level
    except ValueError:
        continue

while True:
    try:
        guess = int(input("Guess: "))  # User's guess
        if guess < random_integer:
            print("Too small!")
        elif guess > random_integer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
       continue
