import csv
import sys

# check if correct argument was given
if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif not sys.argv[1].endswith(".csv"):
    sys.exit("Not a CSV file")
elif not sys.argv[2].endswith(".csv"):
    sys.exit("Not a CSV file")

students = []
names = []
newdict = []

# try to open file with full names and house
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        # append information from csv to list
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

# exit if file with full names does not exist
except FileNotFoundError:
    sys.exit("Could not read " + sys.argv[1])

# in list students grap full name and split in two
for student in students:
    names = student["name"].split(",")
    # append splitted full name and house to dictionary newdict
    newdict.append(
        {"first": names[1].strip(), "last": names[0], "house": student["house"]}
    )

# write infomation from newdict to new csv file
with open(sys.argv[2], "w") as newfile:
    writer = csv.DictWriter(newfile, fieldnames=["first", "last", "house"])
    writer.writeheader()
    for row in newdict:
        writer.writerow(
            {"first": row["first"], "last": row["last"], "house": row["house"]}
        )
