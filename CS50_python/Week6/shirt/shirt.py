import sys
from PIL import Image, ImageOps
import os

# check if correct number of arguments were inputted
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

# grab file names and extensions to compare
arg1_name, ext_arg1 = os.path.splitext(sys.argv[1])
arg2_name, ext_arg2 = os.path.splitext(sys.argv[2])

# check if correct fomrat of files were inputted
if ext_arg1 != ".jpg" and ext_arg1 != ".png":
    sys.exit("Invalid input")
elif ext_arg2 != ".jpg" and ext_arg2 != ".png":
    sys.exit("Invalid output")
# check if input and output file have same extention
elif ext_arg1 != ext_arg2:
    sys.exit("Input and output have different extensions")

# assign images to variables
try:
    shirt = Image.open("shirt.png")
    image = Image.open(sys.argv[1])
except FileNotFoundError:
    sys.exit("Input does not exist")

# resize image to same size
nmuppet = ImageOps.fit(image, shirt.size, centering=(0.5, 0.5))
# add shirt to image
nmuppet.paste(shirt, shirt)
# save edited image
nmuppet.save(sys.argv[2])
