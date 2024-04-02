import re
import sys


def main():
    print(convert(input("Hours: ").strip()))


def convert(s):
    # chech for input format and store if correct
    if matches := re.fullmatch(
        r"(1?[0-9]):?([0-6]?[0-9])? (..) to (1?[0-9]):?([0-6]?[0-9])? (..)", s
    ):
        # check for correct time format
        try:
            # store starting hour as int
            start_hour = int(matches.group(1))

            # store starting minutes
            if matches.group(2):
                # check if minutes in input do not exceed 60
                if int(matches.group(2)) < 60:
                    start_minute = matches.group(2)
                else:
                    raise ValueError
            # store None in starting_minutes if user did not input minutes for starting hour
            else:
                start_minute = matches.group(2)

            # store AM or PM for starting hour
            beginning = matches.group(3)

            # store ending hour as int
            end_hour = int(matches.group(4))

            # store ending minutes
            if matches.group(5):
                # check if minutes in input do not exceed 60
                if int(matches.group(5)) < 60:
                    end_minute = matches.group(5)
                else:
                    raise ValueError
            # store None in ending_minutes if user did not input minutes for ending hour
            else:
                end_minute = matches.group(5)
            # store AM or PM for ending hour
            ending = matches.group(6)
            # check if hours do not exceed 12 in input
            if start_hour > 12 or end_hour > 12:
                raise ValueError
        except:
            raise ValueError

        # if starting hours are PM, add 12 to conver to 24 hour format and add minutes
        if beginning == "PM" and start_minute == None:
            if start_hour == 12:
                start_time = f"{start_hour}:00"
            else:
                start_hour = start_hour + 12
                start_time = f"{start_hour}:00"
        elif beginning == "PM":
            if start_hour == 12:
                start_time = f"{start_hour}:{start_minute}"
            else:
                start_hour = start_hour + 12
                start_time = f"{start_hour}:{start_minute}"
        # if starting hours are AM store starting hour with minutes
        elif beginning == "AM" and start_minute == None:
            if start_hour == 12:
                start_time = "00:00"
            elif int(start_hour) < 10:
                start_time = f"0{start_hour}:00"
            else:
                start_time = f"{start_hour}:00"
        else:
            if start_hour == 12:
                start_time = f"00:{start_minute}"
            elif int(start_hour) < 10:
                start_time = f"0{start_hour}:{start_minute}"
            else:
                start_hour = start_hour + 12
                start_time = f"{start_hour}:{start_minute}"

        # if ending hours are PM, add 12 to conver to 24 hour format and add minutes
        if ending == "PM" and end_minute == None:
            if end_hour == 12:
                end_time = f"{end_hour}:00"
            else:
                end_hour = end_hour + 12
                end_time = f"{end_hour}:00"
        elif ending == "PM":
            if end_hour == 12:
                end_time = f"{end_hour}:{end_minute}"
            else:
                end_hour = end_hour + 12
                end_time = f"{end_hour}:{end_minute}"
        # if ending hours are AM store ending hour with minutes
        elif ending == "AM" and end_minute == None:
            if int(end_hour) == 12:
                end_time = "00:00"
            elif int(end_hour) < 10:
                end_time = f"0{end_hour}:00"
            else:
                end_time = f"{end_hour}:00"
        else:
            if int(end_hour) == 12:
                end_time = f"00:{end_minute}"
            elif int(end_hour) < 10:
                end_time = f"0{end_hour}:{end_minute}"
            else:
                end_hour = end_hour + 12
                if end_hour == 24:
                    end_hour = "00"
                end_time = f"{end_hour}:{end_minute}"
        # store 24 hour time format with correct syntax
        time = f"{start_time} to {end_time}"
        return time
    # raise ValueError if matches not found. Input was in wrong format
    else:
        raise ValueError


if __name__ == "__main__":
    main()
