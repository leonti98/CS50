import random


def main():
    level = get_level()
    score = 0
    for _ in range(1, 11):
        try:
            x = generate_integer(level)
            y = generate_integer(level)
            answer = x + y
            print(f"{x} + {y} = ", end="")
            user_answer = int(input())
            tries = 1
            while user_answer != answer and tries < 3:
                print("EEE")
                tries += 1
                print(f"{x} + {y} = ", end="")
                user_answer = int(input())
                if tries == 3 and user_answer != answer:
                    print("EEE")
                    print(f"{x} + {y} = {answer}")
                    break
            if user_answer == answer:
                score += 1
            if _ == 10:
                print(f"Score: {score}")
        except ValueError:
            continue


def get_level():
    while True:
        try:
            Level = int(input("Level: "))
            # check for correct input
            if Level < 1 or Level > 3:
                raise ValueError
            else:
                return Level
        except ValueError:
            continue


def generate_integer(level):
    if level == 1:
        n = random.randint(0, 9)
    elif level == 2:
        n = random.randint(10, 99)
    else:
        n = random.randint(100, 999)
    return n


if __name__ == "__main__":
    main()
