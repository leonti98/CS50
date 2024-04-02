def main():
    fuel = int(round(get_numbers()))
    if fuel >= 99:
        print ("F")
    elif fuel <= 1:
        print ("E")
    else:
        print (f"{fuel}%")


def get_numbers():
    while True:
        try:
            prompt = (input("Fraction: "))
            number = prompt.split("/")
            x = int(number[0])
            y = int(number[1])
            while x>y:
                prompt = (input("Fraction: "))
                number = prompt.split("/")
                x = int(number[0])
                y = int(number[1])
            f = x/y*100
        except (ValueError, ZeroDivisionError):
            pass
        else:
            break
    return f

main()
