import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 43.135114
MY_LONG = 17.858345

MY_EMAIL = "mailscriptinpython@gmail.com"
MY_PASSWORD = "jfim bdqh lowv sbdz"
REC_EMAIL = "kulasyt@gmail.com"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hours_now = time_now.hour

while True:
    time.sleep(60)
    if int(MY_LAT) == int(iss_latitude) and int(MY_LONG) == int(iss_longitude):
        if hours_now > sunset or hours_now < sunrise:
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.starttls()
                connection.login(MY_EMAIL, MY_PASSWORD)
                connection.sendmail(from_addr = MY_EMAIL,
                                    to_addrs = REC_EMAIL,
                                    msg = "SUBJECT: ISS OVERHEAD!\n\nISS is currently above your location, look up!"
                                    )