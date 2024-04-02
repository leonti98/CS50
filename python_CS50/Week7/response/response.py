import validators


def main():
    print(test(input("What's your email address? ")))


def test(s):
    try:
        email_address = validators.email(s)
        if email_address == True:
            return "Valid"
        else:
            return "Invalid"
    except:
        return "invalid"


if __name__ == "__main__":
    main()
