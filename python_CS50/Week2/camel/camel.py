def main():
    text = camel_list(input("camelCase: "))
    print_snake(text)

def camel_list(myText):
    s = list(myText)
    return s

def print_snake(s):
    for c in range (len(s)):
        if s[c].isupper():
            s[c] = (f"_{s[c].lower()}")
    print("".join(s))

main()
