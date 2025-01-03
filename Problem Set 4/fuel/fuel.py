def get_fuel_percentage():
    while True:
        try:
            fraction = input("Fraction (e.g., X/Y): ")

            num, denom = fraction.split("/")
            num = int(num)
            denom = int(denom)

            if denom == 0:
                raise ZeroDivisionError("Denominator cannot be zero.")
            if num > denom:
                raise ValueError("Numerator cannot be greater than the denominator.")

            percentage = round((num / denom) * 100)

            if percentage <= 1:
                return "E"
            elif percentage >= 99:
                return "F"
            else:
                return f"{percentage}%"

        except ValueError:
            print("Invalid input. Please enter a valid fraction in the format X/Y.")
        except ZeroDivisionError:
            print("Denominator cannot be zero. Please try again.")

if __name__ == "__main__":
    result = get_fuel_percentage()
    print(result)
