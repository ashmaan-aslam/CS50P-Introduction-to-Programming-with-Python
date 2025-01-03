import csv
import sys

# Check for the correct number of command-line arguments
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# Initialize an empty list for storing student data
students = []

# Read the input file
try:
    with open(sys.argv[1]) as input_file:  # Use the first argument for the input file
        reader = csv.DictReader(input_file)  # Read CSV as a dictionary
        for row in reader:
            # Split the "name" column into "first" and "last"
            last, first = row["name"].split(", ")
            # Append the processed data to the students list
            students.append({"first": first, "last": last, "house": row["house"]})
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")  # Exit if the input file is not found

# Write to the output file
with open(sys.argv[2], 'w', newline='') as output_file:  # Use the second argument for the output file
    fieldnames = ["first", "last", "house"]  # Define the field names for the new CSV
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()  # Write the header row
    for student in students:
        writer.writerow(student)  # Write each student's data to the file
