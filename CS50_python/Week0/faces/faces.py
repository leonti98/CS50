def main():
    mytext = input("input your text: ")
    convert(mytext)

def convert(mytext):
    mytext = mytext.replace(":)", "🙂")
    mytext = mytext.replace(":(", "🙁")
    print(mytext)

main()
