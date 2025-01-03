import sys #used for getting arg by user
from PIL import Image #used for opening image
from PIL import ImageOps #used for resizing the image
import os

#checking if the number of arg given is valid
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

#initializing input and output files to args given
input_file = sys.argv[1]
output_file = sys.argv[2]

#extensions that can be used
valid_extensions = ('.jpg', '.jpeg', '.png')

#checking if input and output file have vald]id extensions and are equal to each other
input_ext = os.path.splitext(input_file)[1].lower()
output_ext = os.path.splitext(output_file)[1].lower()
if input_ext not in valid_extensions or output_ext not in valid_extensions:
    sys.exit("Invalid input or output file format")
if input_ext != output_ext:
    sys.exit("Input and output files must have the same extension")

#checking if given file (input_file) exists
try:
    with open(input_file, "rb") as file:
        pass
except FileNotFoundError:
    sys.exit("File Not Found")

#opening the shirt image and the given image
shirt = Image.open("shirt.png")
image = Image.open(sys.argv[1])

#resizing the shirt over the given image
image = ImageOps.fit(image, shirt.size)
image.paste(shirt, shirt)

#saving the shirt resized over the image
image.save(sys.argv[2])
