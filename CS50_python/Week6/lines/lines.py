import sys

# check if correct argument was given
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".py"):
    sys.exit("Not a Python file")

# define counter
n = 0

try:
    with open(sys.argv[1]) as file:
        for line in file:
            # check for empty lines and comments
            if line.lstrip().startswith("#") or len(line.strip()) < 1:
                continue
            # add to counter if all conditions met
            else:
                n += 1
except FileNotFoundError:
    sys.exit("File does not exist")

print(n)
