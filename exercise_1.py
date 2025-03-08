from datetime import date
import re

def current_age():
    str_dob = input("What is your date of birth? Please enter your date of birth in the American format: mm/dd/yyyy\n>")
    regex = re.compile(r'[0-9]{2}/[0-9]{2}/[0-9]{4}')
    result = regex.fullmatch(str_dob)
    date_today = date.today()
    if result:
        lst_chars_dob = str_dob.split("/")
        lst_ints_dob = [int(ele) for ele in lst_chars_dob]
        if lst_ints_dob[0] in list(range(1, 13)):
            if lst_ints_dob[1] in list(range(1, 32)):
                if lst_ints_dob[2] in list(range(1, date_today.year + 1)):
                    formatted_dob = date(int(lst_chars_dob[2]), int(lst_chars_dob[0]), int(lst_chars_dob[1]))
                    if formatted_dob < date_today:
                        days_in_year = 365.2425
                        age = int((date_today - formatted_dob).days / days_in_year)
                        str_msg_1 = f"Today on {str(date_today.day) + "/" + str(date_today.month) + "/" + str(date_today.year)} the User is {age} years"
                        str_msg_2 = f"The User's date of birth in the European format is: {lst_chars_dob[1] + "/" + lst_chars_dob[0] + "/" + lst_chars_dob[2]}"
                        return (str_msg_1 + "\n" + str_msg_2)

    return f"The date of birth you have entered of {str_dob} is inappropriate"


print(current_age())