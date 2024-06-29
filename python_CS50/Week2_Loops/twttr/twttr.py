def main():
    tweet = transform_twttr(input("Input: "))
    print (tweet)

def transform_twttr(tweet):
    twttr = ""
    for c in tweet:
        match c:
            case "A" | "E" | "I" | "O" | "U":
                continue
            case "a" | "e" | "i" | "o" | "u":
                continue
            case _:
                twttr = twttr + c
    return twttr

main()
