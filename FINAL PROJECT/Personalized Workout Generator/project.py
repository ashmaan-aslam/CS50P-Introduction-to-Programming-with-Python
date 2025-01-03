# Personalized Workout Generator

import random
import json
import os

def main():
    print("Welcome to the Fitplan!")

    exercises = load_exercises("exercises.txt")
    if not exercises:
        return

    while True:
        print("\nMain Menu:")
        print("1. Create a new workout plan")
        print("2. Load a saved workout plan")
        print("3. Exit")

        choice = get_user_input("Choose and option (1/2/3): ", ["1", "2", "3"])

        if choice == "1":
            #getting user preferences for workout
            workout_type = get_user_input("Enter workout type (Cardio/Strength/Flexibility): ", ["Cardio", "Strength", "Flexibility"])
            difficulty = get_user_input("Enter difficulty (Easy/Medium/Hard): ", ["Easy", "Medium", "Hard"])
            duration = int(get_user_input("Enter duration (in minutes): "))

            #generating workout based on user input
            workout_plan = gen_workout(exercises, workout_type, difficulty, duration)
            if workout_plan:
                display_workout(workout_plan)

                #asking user if they want to save the plan
                save_option = get_user_input("Would you like to save this workout? (yes)/(no) ", ["Yes", "No"])
                if save_option == "Yes":
                    save_workout(workout_plan, "saved_workout.json")

        elif choice == "2":
            #load and display a saved workout plan
            workout_plan = load_workout("saved_workout.json")
            if workout_plan:
                display_workout(workout_plan)

        elif choice == "3":
            print("Goodbye!")
            break

def load_exercises(file_path):
    '''
    load the exercise data from the file and return it as list of exercises [type, name, difficulty, duration]
    '''

    exercises = []
    try:
        with open(file_path) as file:
            for line in file:
                exercises.append(line.strip().split(","))
    except FileNotFoundError:
        print("Exercise data file not found!")
    return exercises

def get_user_input(prompt, valid_options=None):
    '''
    to get input from the user, validate it and return it.
    if valid_options is given, ensure the input will be in that list
    '''
    while True:
        try:
            user_input = input(prompt).strip().title()
            if valid_options and user_input not in valid_options:
                raise ValueError(f"Please choose from {valid_options}")
            return user_input
        except ValueError as e:
            print(e)

def gen_workout(exercises, workout_type, difficulty, total_duration):
    '''
    Generate a personalized workout plan based on user's input. Exercises are filtered by type and difficulty.
    '''
    workout_plan = []
    filtered_exercises = [ex for ex in exercises if ex[0] == workout_type and ex[2] == difficulty]

    while total_duration > 0 and filtered_exercises:
        # Pick an exercise that fits within the remaining duration
        valid_exercises = [ex for ex in filtered_exercises if int(ex[3].split()[0]) <= total_duration]
        if not valid_exercises:
            break  # Stop if no exercise fits the remaining time

        exercise = random.choice(valid_exercises)
        workout_plan.append(exercise)
        duration = int(exercise[3].split()[0])
        total_duration -= duration

    return workout_plan

def display_workout(workout_plan):
    '''
    display the details of workout
    '''
    print("\nYour personalized workout plan:")
    for exercise in workout_plan:
        print(f"{exercise[1]} - {exercise[3]} ({exercise[2]})")

def save_workout(workout_plan, file_path):
    '''
    save the workout plan to a file
    '''
    try:
        with open(file_path, "w") as file:
            json.dump(workout_plan, file)
        print("Workout plan saved successfully!")
    except Exception as e:
        print(f"Error saving workout plan: {e}")

def load_workout(file_path):
    '''
    load saved workout plan from file
    '''
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("No saved workout plan found.")
        return []

if __name__ == "__main__":
    main()
