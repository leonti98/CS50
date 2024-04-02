def main():
    txt = input("Text: ")
    grade = check_grade(txt)
    if grade < 1:
        print(f"Before Grade 1")
    elif grade >= 16:
        print(f"Grade 16+")
    else:
        print(f"Grade: {grade}")


def check_grade(txt):
    sentence_counter = 0
    # intialize word_counter as 1 to include last word
    word_counter = 1
    letter_counter = 0
    for c in txt:
        if c == "." or c == "!" or c == "?":
            sentence_counter += 1
        elif c == " ":
            word_counter += 1
        elif c.isalpha():
            letter_counter += 1

    L = round(letter_counter / word_counter * 100, 2)
    S = round(sentence_counter / word_counter * 100, 2)

    index = round(0.0588 * L - 0.296 * S - 15.8)

    return index

if __name__ == "__main__":
    main()
