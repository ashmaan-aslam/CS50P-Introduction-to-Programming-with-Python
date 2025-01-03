import sys

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

filename = sys.argv[1]
count = 0

if not filename.endswith(".py"):
    sys.exit("File does not exist")
try:
    with open(sys.argv[1]) as file:
        for lines in file:
            if lines.strip() and not lines.strip().startswith("#"):
                count += 1
except FileNotFoundError:
    sys.exit("File not Found")

print(count)
