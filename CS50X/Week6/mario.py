while True:
    height = input("Height: ")
    try:
        height = int(height)
    except:
        continue
    if height > 8:
        continue
    break

brick = "#"
space = " "
n = height

while True:
    print(space * (n - 1), end="")
    print(brick * (height - n + 1), end="")
    n -= 1
    print("  ", end="")
    print(brick * (height - n))
    if n == 0:
        break
