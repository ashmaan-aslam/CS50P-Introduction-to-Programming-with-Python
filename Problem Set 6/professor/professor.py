import random

def main():
    score = 0  # User's score
    level = get_level()  # Prompt for difficulty level

    for _ in range(10):  # Loop for 10 problems
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y

        attempts = 0
        while attempts < 3:  # Allow 3 attempts per problem
            try:
                # Prompt for user input
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == correct_answer:  # Correct answer
                    score += 1
                    break
                else:  # Incorrect answer
                    print("EEE")  # Feedback for wrong answer
                    attempts += 1
            except ValueError:  # Invalid input
                print("EEE")  # Feedback for invalid input
                attempts += 1

        # Display correct answer after 3 incorrect attempts
        if attempts == 3:
            print(f"The correct answer is: {correct_answer}")

    # Display final score (expected format)
    print(score)

def get_level(): # amount of difficulty
    while True:
        try:
            input_level = int(input("Level: ")) # user input of difficulty
            if input_level in [1, 2, 3]:
                return input_level
            else:
                continue
        except ValueError:
            continue


def generate_integer(level):

    if level not in [1, 2, 3]: # amount of number being gen due to level
        raise ValueError("Level must be 1, 2, or 3.")
    elif level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
