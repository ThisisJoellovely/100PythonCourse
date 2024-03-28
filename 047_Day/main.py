import requests
import smtplib
import os
from dotenv import load_dotenv
import lxml
from bs4 import BeautifulSoup

load_dotenv("/Users/lovely/Documents/Udemy/SECRET_API_KEYS/047_Day/.env")
SENDER_EMAIL = os.environ.get("SENDER_EMAIL")
SENDER_PASSWORD = os.environ.get("SENDER_PASSWORD")

# Constants 
HEADER = {
    'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept-Language' : 'en-US,en;q=0.9'
} 
URL = "https://www.amazon.com/Fujifilm-X-S20-Mirrorless-Camera-Body/dp/B0C5PHCFRQ/ref=sr_1_1?crid=LIMPXGVGMHNR&dib=eyJ2IjoiMSJ9.2nFQMQbWJY4DRPyWLmWrtE-HuzxdCKVii7yWAGbGUO8jYCnvg27MYs5bth8HSA2ZmT1peewOk5jOT-WLekQKm1aX7A8ryJmRCr6fmxG83N9EQ4jpLcVR1kWSnaW1G77600wiVz90nFHWjkS_-dHbwg.tBDJGyeJTVvzmFX2oz0Xn0W-ReMQrRwIuq-IrIXp9Zs&dib_tag=se&keywords=fuji%2Bmax%2Bxs-20&qid=1711560825&sprefix=fuji%2Bmax%2Bxs-20%2Caps%2C104&sr=8-1&th=1"
WILLING_AMOUNT = 1400


SENDER_EMAIL = os.environ.get

 
try:
    response = requests.get(URL, headers=HEADER) 
    if response.status_code == 200: 
        amazonCameraXS20_HTML = response.text
    else:
        raise Exception(f"Request failed with status code: {response.status_code}")
except requests.RequestException as e: 
   print(f"ERROR in the connecting to API endpoint: {e}")

soup = BeautifulSoup(amazonCameraXS20_HTML, "lxml")

productTitle_html = soup.find("span", class_="a-size-large product-title-word-break", id="productTitle")
price_html = soup.find("span", class_="a-price-whole")

if productTitle_html:
    productTitle_text = (productTitle_html.text.strip())
else:
    exit("Product_Title not found")

if price_html:
    price_text = (price_html.text.strip()).replace(",","")
    try:
        price_float = float(price_text)
    except ValueError:
        print(f"Value Error")
else:
    exit("Price not found")

if(price_float <= WILLING_AMOUNT):
    with smtplib.SMTP("smtp.gmail.com",25) as connection:
        connection.starttls()
        connection.login(user=SENDER_EMAIL, password=SENDER_PASSWORD)
        connection.send_message(
            to_addrs="joellovely@icloud.com",
            from_addr=SENDER_EMAIL,
            msg=f"Subject: Price DROP!{productTitle_text}!\n\nPrice: ${price_float}"
        )
    









