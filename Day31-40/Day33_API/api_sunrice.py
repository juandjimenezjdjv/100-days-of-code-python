import requests
from datetime import datetime
import smtplib
import time

EMAIL: "hola@email.com"
PASSWORD: "hola"

MY_LAT = 9.748917
MY_LON = -83.753426

def iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status
    data = response.json()

    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_lat <= MY_LAT+5 and MY_LON-5 <= iss_lng <= MY_LON+5:
        return True

def is_nigth():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LON,
        "formatted": 0,
        }

    r = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    r.raise_for_status()
    data = r.json()

    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if time_now >= sunset  or time_now <=  sunrise:
        return True

while True:
    time.sleep(60)
    if iss_overhead() and is_nigth():
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg="Subject: Look up\n\nThe ISS is above you in the sky."
        )
