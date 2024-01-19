# Motivational monday quotes implementation 
import smtplib 
import datetime
import random
from email.mime.text import MIMEText

#CONSTANTS
QUOTES_FILE_PATH = "/Users/lovely/Documents/100_DaysOfProgramming/032_Day/Quotes.csv"
MY_EMAIL = "thisisfortesting@gmail.com"
PASSWORD = "arbituary password"

MY_OTHER_EMAIL = "thisisfortesting@gmail.com"



# Implementation to figure out what day it is 
def get_day():
    time_now = datetime.datetime.now()
    weekday = time_now.weekday()
    return weekday

# Implementation to read file full of quotes
def read_file():
    with open(QUOTES_FILE_PATH) as file:
        file_read = file.readlines()
        random_quote = random.choice(file_read)
    
    return random_quote

# Implementation of sending email 

if (get_day() == 3):
    random_quote = read_file()
    random_quote_main = f"Subject:Thursday APPROACHING:\n\nHey guys this is an automated message,\n{random_quote}\nBe Safe, Joel Lovely"
    random_quote_main = MIMEText(random_quote_main,'plain','utf-8')
    
    with  smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(to_addrs=MY_OTHER_EMAIL,
                            from_addr=MY_EMAIL,
                            msg = random_quote_main
        )
        connection.close() 





