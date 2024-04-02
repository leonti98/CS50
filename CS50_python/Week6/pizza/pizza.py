import sys
import csv
from tabulate import tabulate

# check if correct argument was given
if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")

menu = {}

# try to format and print file
try:
    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        print(reader)
        print(tabulate(reader, headers="firstrow", tablefmt="grid"))
# if file does not exist exit
except FileNotFoundError:
    sys.exit("File does not exist")
