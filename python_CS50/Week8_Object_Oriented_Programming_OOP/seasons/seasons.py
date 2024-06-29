from datetime import date
import inflect
import re
import sys

p = inflect.engine()


def main():
    print(get_difference(input("Date of Birth: ")))


def get_difference(d):
    today = date.today()
    if matches := re.fullmatch(r"(\d\d\d\d)-(\d\d)-(\d\d)", d):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        birth = date(year, month, day)
    else:
        sys.exit("Invalid date")
    difference = today - birth
    minutes = difference.days * 1440
    time_passed = f"{p.number_to_words(minutes, andword="")} minutes"
    return time_passed.capitalize()


if __name__ == "__main__":
    main()
