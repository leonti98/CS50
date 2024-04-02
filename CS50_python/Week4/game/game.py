import random

while True:
    try:
        level = int(input("Level: "))
        if level < 1:
            continue
        else:
            break
    except ValueError:
        continue

guess_number = random.randint(1, level)

while True:
    try:
        user_guess = int(input("Guess: "))
        # check for correct input
        if user_guess < 1 or user_guess > level:
            continue
        # check user if input matches
        if user_guess == guess_number:
            print("Just right!")
            break
        elif user_guess < guess_number:
            print("Too small!")
            continue
        else:
            print("Too large!")
            continue

    except ValueError:
        continue
