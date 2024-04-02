def main():
    tweet = shorten(input("Input: "))
    print (tweet)

def shorten(word):
    twttr = ""
    for c in word:
        match c:
            #case "A" | "E" | "I" | "O" | "U":
                #continue
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                twttr = twttr + c
    return twttr

if __name__ == "__main__":
    main()
