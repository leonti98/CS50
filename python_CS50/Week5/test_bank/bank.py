def main():
    answer = value(input("Greeting : "))
    print(f"${answer}")


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting[0:5] == ("hello"):
        return 100
    elif greeting[0] == "h":
        return 0
    else:
        return 100


if __name__ == "__main__":
    main()
