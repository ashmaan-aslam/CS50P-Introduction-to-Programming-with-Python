def main():
    while True:
        try:
            fraction = input("Fraction (e.g., X/Y): ")
            percentage = convert(fraction)
            print(gauge(percentage))
            break
        except (ValueError, ZeroDivisionError) as e:
            print(e)


def convert(fraction):
    try:
        num, denom = fraction.split("/")
        num = int(num)
        denom = int(denom)

        if denom == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")
        if num > denom:
            raise ValueError("Numerator cannot be greater than the denominator.")

        return round((num / denom) * 100)
    except (ValueError, ZeroDivisionError):
        raise


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
