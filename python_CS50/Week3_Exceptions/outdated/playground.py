def main():
    date = get_date()
    print (date)

def get_date():
    while True:
        month_dict = {
                    "January": 1, "February": 2, "March": 3,
                    "April": 4, "May": 5, "June": 6, "July": 7,
                    "August": 8, "September": 9, "October": 10,
                    "November": 11, "December": 12,
                    }
        try:
            date = (input("Date: "))
            #check if date is in correct form
            if "/" in date or "," in date:
                #remove delimiters and make new list without
                date_list = date.split("/")
                if date_list[0].isalpha() and "/" in date:
                    continue
                else:
                    delimiters = ["/", " ", ","]
                    for delimiter in delimiters:
                        date = " ".join(date.split(delimiter))
                        date_list = date.split()
                #check if input was real date, else start ask again
                if int(date_list[1]) <= 31 and int(date_list[0]) <= 12:
                    #adding to list in right order
                    iso_date = ["0", "0", "0"]
                    #year
                    iso_date[0] = f"{int(date_list[2])}"
                    #month
                    iso_date[1] = f"{int(date_list[0]):02}"
                    #day
                    iso_date[2] = f"{int(date_list[1]):02}"
                    str_iso_date = "-".join(iso_date)
                    return str_iso_date

        except ValueError:
            dete_list = date.split(" ")
            #check if input month exists, else restart
            if date_list[0] in month_dict:
                date_list[0] = (month_dict[date_list[0]])
                #check if input was real date, else start ask again
                if int(date_list[1]) <= 31 and int(date_list[0]) <= 12:
                    #adding to list in right order
                    iso_date = ["0", "0", "0"]
                    #year
                    iso_date[0] = f"{int(date_list[2])}"
                    #month
                    iso_date[1] = f"{int(date_list[0]):02}"
                    #day
                    iso_date[2] = f"{int(date_list[1]):02}"
                    str_iso_date = "-".join(iso_date)
                    #print (date_list)
                    #print (date_list[0])
                    return str_iso_date




main()
