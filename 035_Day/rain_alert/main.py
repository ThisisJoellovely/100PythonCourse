# Import Statements
import requests
import json
from twilio.rest import Client

# Constants 
# Recovery ID LUVKF6FH6GDYGRHJZPKMYNUJ
ACCOUNT_SID = "ACbaf4f482cdabab51d8d479f32a134ded"
AUTHORIZATION_TOKEN = "7772f969dd7f51c979e36f9e5a0d1281"
WEATHER_URL = "http://api.openweathermap.org/data/2.5/forecast"
API_KEY = "e87884a8cd389c08b9ecf1fac59327e1"
PARAMETERS = {
    "lat" : 42.053101,
    "lon" : -87.976196,
    "cnt" : 4, 
    "appid" : API_KEY
}

connection = requests.get( WEATHER_URL , PARAMETERS) 
connection.raise_for_status()
weather_data = connection.json()
weather_truth = False

for hour_data in  weather_data["list"]:
   conditon_code = hour_data["weather"][0]["id"]
   if int(conditon_code < 700):
      weather_truth = True


if weather_truth == True:
   client = Client(AUTHORIZATION_TOKEN, ACCOUNT_SID)
   message = client.messages.create(
      body ="It's going to rain today, bring an umbrella" ,
      from_ ="+18442799858",
      to ='8478639136'
   )
   print(message.status)

if weather_truth == False:
   client = Client(AUTHORIZATION_TOKEN, ACCOUNT_SID)
   message = client.messages.create(
      body ="It's going to be sunny don't worry about bringing a umbrella" ,
      from_ ="+18442799858",
      to ='8478639136'
   )
   print(message.status)






test = 0
    
    
