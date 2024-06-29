import re

name = input("What's your name? ").strip()
if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.groups(2)} {matches.groups(1)}"
print(f"hello, {name}")
