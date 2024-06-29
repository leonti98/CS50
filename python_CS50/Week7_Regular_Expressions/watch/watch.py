import re
import sys


def main():
    print(parse(input("HTML: ").strip()))


def parse(s):
    # search input for link and store
    matches = re.search(
        r"\"https?://(www\.)?(youtube\.com\/embed\/([a-zA-Z0-9]+))\"", s
    )
    if matches:
        # store (youtube\.com\/embed\/([a-zA-Z0-9]+)) this part in link
        link = matches.group(2)
        # change to shorter link with https
        new_link = link.replace("youtube.com/embed/", "https://youtu.be/")
        return new_link
    # return None if link was not found


if __name__ == "__main__":
    main()
