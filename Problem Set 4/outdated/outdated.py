months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    date = input("Date: ").strip()

    # Handle MM/DD/YYYY format
    if "/" in date and len(date.split('/')) == 3:
        month, day, year = date.split('/')
        if month.isdigit() and day.isdigit() and year.isdigit() and 1 <= int(month) <= 12 and 1 <= int(day) <= 31:
            print(f"{year}-{int(month):02}-{int(day):02}")
            break
        else:
            continue

    # Handle Month Day, Year format
    elif "," in date and any(month in date for month in months):
        date = date.replace(",", "").split()
        month, day, year = date[0], date[1], date[2]
        if month in months and day.isdigit() and year.isdigit() and 1 <= int(day) <= 31:
            month_index = months.index(month) + 1
            print(f"{year}-{int(month_index):02}-{int(day):02}")
            break
        else:
            continue

    # Invalid input, prompt again
    else:
        continue
