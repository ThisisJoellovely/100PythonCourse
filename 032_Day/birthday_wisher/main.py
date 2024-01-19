##################### Hard Starting Project ######################

# 1. Update the birthdays.csv with your friends & family's details. 
# HINT: Make sure one of the entries matches today's date for testing purposes.
# DONE 

# 2. Check if today matches a birthday in the birthdays.csv
# HINT 1: Only the month and day matter. 
# HINT 2: You could create a dictionary from birthdays.csv that looks like this:
# birthdays_dict = {
#     (month, day): data_row
# }
#HINT 3: Then you could compare and see if today's month/day matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
# HINT: https://www.w3schools.com/python/ref_string_replace.asp

# 4. Send the letter generated in step 3 to that person's email address.
# HINT: Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)

import smtplib 
import datetime 
import pandas
import random

# Constants
birthday_dict = {}
FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/032_Day/birthday_wisher/birthdays.csv"
TODAYS_DAY = (datetime.datetime.now().month, datetime.datetime.now().day)
USER = "Joellovely0717@gmail.com"
PASSWORD = "ubbugsuvxmdmkbsg"


# Implementation of reading file and saving into a dictionary where a tuple of month and day is the key 
def read_file():
    global birthday_dict
    data = pandas.read_csv(FILE_PATH)
    birthday_dict = {(row["month"], row["day"]): row for index, row in data.iterrows()}
read_file()

# Implementation if today is the birthday
if TODAYS_DAY in birthday_dict:
    birthday = birthday_dict[TODAYS_DAY]
    with open(f"/Users/lovely/Documents/100_DaysOfProgramming/032_Day/birthday_wisher/letter_templates/letter_{random.randint(1,3)}.txt") as file:
        contents = file.read()
        contents.replace("[NAME]" , birthday["name"])

    
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=USER, password=PASSWORD)
        connection.send_message(
            to_addrs=birthday["email"],
            from_addr=USER,
            msg=f"Subject: Happy Birthday!\n\n{contents}"
        )
        
    

