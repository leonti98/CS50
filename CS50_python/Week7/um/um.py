import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    found = re.findall(r"(\bum\b)", s, re.IGNORECASE)
    print(found)
    return len(found)


if __name__ == "__main__":
    main()
