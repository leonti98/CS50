def main():
    time = convert(input("What time is it? "))
    if time >= 7 and time <= 8:
        print ("breakfast time")
    elif time >= 12 and time <= 13:
        print ("lunch time")
    elif time >= 18 and time <= 19:
        print ("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)/60
    time = hours+minutes
    return time


if __name__ == "__main__":
    main()


#Suppose that you’re in a country where it’s customary to eat breakfast between 7:00 and 8:00, lunch between 12:00 and 13:00, and dinner between 18:00 and 19:00. Wouldn’t it be nice if you had a program that could tell you what to eat when?
