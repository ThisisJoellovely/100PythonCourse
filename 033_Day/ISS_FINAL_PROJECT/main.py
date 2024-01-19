import requests
import smtplib
from datetime import datetime


MY_LAT = 0# Your latitude
MY_LONG = 0 # Your longitude
MY_EMAIL = "thisisfortesting@gmail.com"
MY_PASSWORD = "arbitrary password"

PARAMETERS = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# One time implementation of checking if current location is between +5 or -5 of the International Space Station using check as a helper function
def check(tuple):
    abs_lat = abs(tuple[0])
    abs_long = abs(tuple[1])
    if (abs_lat - 5) <= abs(MY_LAT) <= (abs_lat + 5) and (abs_long - 5 <= abs(MY_LONG) <= abs_long + 5):
        return True
    else:
        return False
    
with requests.get(url="http://api.open-notify.org/iss-now.json") as response_stage1:
    response_stage1.raise_for_status()
    data = response_stage1.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if (check((iss_latitude,iss_longitude)) == True):
        with requests.get("https://api.sunrise-sunset.org/json", params=PARAMETERS) as response_stage2:
            response_stage2.raise_for_status()
            data = response_stage2.json()
            sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
            sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
            time_now = 8 #datetime.now().hour
            if(sunset <= time_now <= sunrise):
                with smtplib.SMTP("smtp.gmail.com",) as response_stage3:
                    response_stage3.starttls()
                    response_stage3.login(user=MY_EMAIL,password=MY_PASSWORD)
                    response_stage3.sendmail(
                        to_addrs=MY_EMAIL,
                        from_addr=MY_EMAIL, 
                        msg="SUBJECT:ISS IS ABOVE US!:\n\n Since it's night time this is the perfect time to check this out!"
                    )
    elif (check((iss_latitude,iss_longitude)) == False):
        print("The ISS is not near the current location you are positioned")





