from datetime import date
import inflect
import sys

def main():
    # Ask the user for their date of birth
    inpt = input('Date of Birth (YYYY-MM-DD): ')
    # Print how old they are in minutes by calling get_age_in_minutes
    print(get_age_in_minutes(inpt))

def get_age_in_minutes(inpt):
    # Try to convert the input into a date
    try:
        bday = date.fromisoformat(inpt)  # Parse the date string into a date object
    except ValueError:
        # Exit with an error message if the date is not valid
        sys.exit('Invalid date format. Please enter in YYYY-MM-DD format.')

    # Get today's date
    today = date.today()

    # Calculate the difference between today and the birthday
    diff = today - bday
    no_of_days = diff.days

    # Exit if the birthday is in the future
    if no_of_days < 0:
        sys.exit('The date of birth cannot be in the future.')

    # Convert the number of days into minutes
    minutes = no_of_days * 24 * 60

    # Convert the minutes into words using inflect
    inf = inflect.engine()
    min_words = inf.number_to_words(minutes)

    # Remove 'and' from the words and capitalize the first letter
    min_words = min_words.replace(' and', '').capitalize()

    # Return the result with 'minutes' at the end
    return min_words + ' minutes'

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()
