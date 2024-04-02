name = input("what's yout name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Griffindor")
    case "Drako":
        print("Slythering")
    case _:
        print("Who?")
