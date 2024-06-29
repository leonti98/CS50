import re
import sys


def main():
    while True:
        number = input("Number: ").strip()
        try:
            int(number)
            break
        except:
            continue
    is_valid = validate(number)
    if is_valid == False:
        sys.exit("INVALID")
    else:
        print(is_valid)


def validate(s):
    if len(s) < 13 or len(s) > 16:
        return False
    elif len(s) == 14:
        return False
    # check if checksome ends with 0
    check = checksum(s)
    if check == False:
        sys.exit("INVALID")
    # check if pattern matches any card issuer
    if matches := re.match(r"^(4|5[1-5]|3[4|7])", s):
        if matches.group(1)[0] == "4" and (len(s) == 13 or len(s) == 16):
            return "VISA"
        elif matches.group(1)[0] == "3" and len(s) == 15:
            return "AMEX"
        elif matches.group(1)[0] == "5" and len(s) == 16:
            return "MASTERCARD"
        else:
            return False
    else:
        return False


def checksum(number):
    i = 0
    sum_first = 0
    sum_second = 0
    # reverse card number
    number = number[::-1]

    for digit in number:
        digit = int(digit)

        # every second from first
        if i % 2 == 1:
            if digit * 2 > 9:
                sum_first += int(str(digit * 2)[0])
                sum_first += int(str(digit * 2)[1])
            else:
                sum_first += digit * 2
        # every second after second
        else:
            sum_second += digit
        i += 1

    total = sum_first + sum_second
    if total % 10 == 0:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
