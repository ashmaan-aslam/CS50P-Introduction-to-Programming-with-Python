import sys
from tabulate import tabulate
import csv

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]

if not filename.endswith(".csv"):
    sys.exit("Not a CSV file")

try:
    with open(filename) as file:
        reader = csv.reader(file)
        header = next(reader)
        row = list(reader)
except FileNotFoundError:
    sys.exit("File not found")

table = tabulate(row, header, tablefmt = "grid")

print(table)
