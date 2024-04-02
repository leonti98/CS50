def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 2 <= len(s) <= 6 and s[1].isalpha and s[2].isalpha:
        for c in range(len(s)):
            if s[c].isalpha():
                continue
            elif s[c].isnumeric() and s[c] != "0":
                if s[c+1:].isnumeric():
                    return True
                else:
                    return False
            else:
                return False
        return True
    else:
        return True

if __name__ == "__main__":
    main()

