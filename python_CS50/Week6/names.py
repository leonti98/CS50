names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.strip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")


"""
with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line.strip())
"""


"""
name = input("what's your name? ")

with open("names.txt", "a") as file:
    file.write(f"{name}\n")
"""


# file = open("names.txt", "a")
# file.close


"""
names = []
for _ in range (3):
    names.append(input("What's ypur name? "))

for name in sorted(names):
    print(f"hello, {name}")
"""
