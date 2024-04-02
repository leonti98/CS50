def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(plate):
    if 2 <= len(plate) <= 6 and plate[1].isalpha and plate[2].isalpha:
        for c in range(len(plate)):
            if plate[c].isalpha():
                continue
            elif plate[c].isnumeric() and plate[c] != "0":
                if plate[c+1:].isnumeric():
                    return True
                else:
                    return False
            else:
                return False
        return True
    return False

if __name__ == "__main__":
    main()
