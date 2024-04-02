import random
import sys
from pyfiglet import Figlet

try:
    if len(sys.argv) == 2 or len(sys.argv) > 3:
        sys.exit("Invalid usage 1")
    elif sys.argv[1] not in ["-f", "--font"]:
        sys.exit("Invalid usage 2")
except IndexError:
    pass

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) == 1:
    text = input("Input: ")
    random.shuffle(fonts)
    figlet.setFont(font=fonts[0])
    print(figlet.renderText(text))
elif len(sys.argv) == 3 and sys.argv[2] in fonts:
    text = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print("Output: " + figlet.renderText(text))
else:
    sys.exit("Invalid usage")
