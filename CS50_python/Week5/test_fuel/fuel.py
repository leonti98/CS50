def main():
    fuel = convert((input("Fraction: ")))
    print (gauge(fuel))


def convert(fraction):
    while True:
        number = fraction.split("/")
        if int(number[1]) == 0:
            raise ZeroDivisionError
        try:
            x = int(number[0])
            y = int(number[1])
            while x>y:
                raise ValueError
            f = x/y*100
        except (ValueError):
            raise ValueError
        else:
            break
    return int(round(f))


def gauge(percentage):
    if percentage >= 99:
        return ("F")
    elif percentage <= 1:
        return ("E")
    else:
        return (f"{percentage}%")


if __name__ == "__main__":
    main()

