def main():
    mealtime = input(str("What time is it? "))
    mealtime1 = convert(mealtime)

    if 7 <= mealtime1 <= 8:
        print("breakfast time")
    elif 12 <= mealtime1 <= 13:
        print("lunch time")
    elif 18 <= mealtime1 <= 19:
        print("dinner time")
    else:
        print("")


def convert(time):
    time = str(time)
    hours, minutes = time.split(":")

    hours = float(hours)
    minutes = float(minutes)

    totaltime = ((hours * 60) + minutes) / 60
    return totaltime


if __name__ == "__main__":
    main()
