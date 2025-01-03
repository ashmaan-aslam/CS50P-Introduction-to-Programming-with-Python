import pytest
import os
import json
from project import load_exercises, get_user_input, gen_workout, display_workout, save_workout, load_workout

# Test for load_exercises function
def test_load_exercises():
    # Create a temporary exercise file for testing
    file_content = "Cardio,Running,Easy,10 mins\nStrength,Push-Ups,Medium,15 mins\n"
    file_path = "test_exercises.txt"
    with open(file_path, "w") as file:
        file.write(file_content)

    exercises = load_exercises(file_path)
    os.remove(file_path)

    # Verify the exercises are loaded correctly
    assert len(exercises) == 2
    assert exercises[0] == ["Cardio", "Running", "Easy", "10 mins"]
    assert exercises[1] == ["Strength", "Push-Ups", "Medium", "15 mins"]

# Test for get_user_input function
def test_get_user_input(monkeypatch):
    # Simulate user input for valid options
    monkeypatch.setattr('builtins.input', lambda _: "Cardio")
    result = get_user_input("Enter workout type: ", ["Cardio", "Strength", "Flexibility"])
    assert result == "Cardio"

    # Simulate invalid input followed by valid input
    inputs = iter(["invalid", "Strength"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    result = get_user_input("Enter workout type: ", ["Cardio", "Strength", "Flexibility"])
    assert result == "Strength"

# Test for gen_workout function
def test_gen_workout():
    exercises = [
        ["Cardio", "Running", "Easy", "10 mins"],
        ["Cardio", "Cycling", "Easy", "15 mins"],
        ["Strength", "Push-Ups", "Medium", "15 mins"]
    ]
    workout_plan = gen_workout(exercises, "Cardio", "Easy", 20)

    # Verify the generated workout matches the total duration
    assert len(workout_plan) > 0
    total_duration = sum(int(ex[3].split()[0]) for ex in workout_plan)
    assert total_duration <= 20

# Test for display_workout function (mocking print output)
def test_display_workout(capfd):
    workout_plan = [
        ["Cardio", "Running", "Easy", "10 mins"],
        ["Strength", "Push-Ups", "Medium", "15 mins"]
    ]
    display_workout(workout_plan)

    # Capture the printed output
    captured = capfd.readouterr()
    assert "Running - 10 mins (Easy)" in captured.out
    assert "Push-Ups - 15 mins (Medium)" in captured.out

# Test for save_workout function
def test_save_workout():
    workout_plan = [
        ["Cardio", "Running", "Easy", "10 mins"],
        ["Strength", "Push-Ups", "Medium", "15 mins"]
    ]
    file_path = "test_saved_workout.json"

    # Save the workout and verify the file contents
    save_workout(workout_plan, file_path)
    with open(file_path, "r") as file:
        data = json.load(file)

    os.remove(file_path)
    assert data == workout_plan

# Test for load_workout function
def test_load_workout():
    workout_plan = [
        ["Cardio", "Running", "Easy", "10 mins"],
        ["Strength", "Push-Ups", "Medium", "15 mins"]
    ]
    file_path = "test_saved_workout.json"

    # Save a workout to a file
    with open(file_path, "w") as file:
        json.dump(workout_plan, file)

    # Load the workout and verify the contents
    loaded_workout = load_workout(file_path)
    os.remove(file_path)
    assert loaded_workout == workout_plan

    # Test for file not found
    assert load_workout("non_existent_file.json") == []
