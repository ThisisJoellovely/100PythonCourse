import requests
import json 
from datetime import datetime , timedelta

# Constants
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"


daily_dictonary = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME, 
}

news_dictonary = {
    "q" : COMPANY_NAME,
    "searchIn" : "title"
}

# Functions
def read_secret_api(string, file , dictonary):
    """Function Grabs api-password"""
    with open(f"/Users/lovely/Documents/Udemy/SECRET_API_KEYS/{file}") as file:
        api_key = file.read()
    dictonary[string] = api_key
    return dictonary
daily_dictonary = read_secret_api(string="apikey", file="aplhaavantage.txt", dictonary=daily_dictonary)
news_dictonary = read_secret_api(string="apikey", file="newsapi.txt", dictonary=news_dictonary)

def get_daily_contents():
    """Function gets the json package from the Stock API and filters dictonary for daily content"""
    try:
        connection = requests.get(STOCK_ENDPOINT, params=daily_dictonary)
        connection.raise_for_status() 
    except requests.exceptions.HTTPError as e:
        print("An unexpected error has happened: ", e)
    else:
        contents = connection.json()
        return contents["Time Series (Daily)"]


def get_news_content():
    """Function """
    try:
        connection = requests.get(NEWS_ENDPOINT, params=news_dictonary)
        connection.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print("An unexpected error has happened: ", e)
    else:
        contents = connection.json()
        return contents["articles"]

def get_today():
    """Function returns the date"""
    date = datetime.now().date()
    return date

def get_days_away_date(date , d):
    """Function returns the date difference between date and the user specified d"""
    new_date = date - timedelta(days=d)
    return new_date

def positive_difference(n1 , n2):
    "returns the positive difference between two numbers"
    return round(abs(n2 - n1),2)

def percent_difference(diff , total):
    """return the percentage of the difference based on the total"""
    return round(((diff / total) * 100),2)

def printed_textmessage(company_name , p , h_a , d_a):
    print(f"{company_name}: {p}% Difference")
    for i in range(3):
        print(f"Headline: {h_a[i]}")
        print(f"Breif: {d_a[i]}")
        print("\n")

def part_1():
    contents = get_daily_contents()
    closing_price = [contents[(get_days_away_date(get_today() , item)).strftime("%Y-%m-%d")]["4. close"] for item in range(1,3)]
    closing_price = [round(float(price),2) for price in closing_price] 
    d1 = positive_difference(closing_price[0], closing_price[1])
    percent_d1 = percent_difference(d1, closing_price[1])
    return percent_d1

def part_2():
    contents = get_news_content()
    sliced_three = contents[:3]
    sliced_three_headline = [item["title"] for item in sliced_three]
    sliced_three_description = [item["description"] for item in sliced_three]
    printed_textmessage(STOCK_NAME, percent_difference_telsa, sliced_three_headline, sliced_three_description)



percent_difference_telsa = part_1()
part_2() # Will print out the results!




"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

