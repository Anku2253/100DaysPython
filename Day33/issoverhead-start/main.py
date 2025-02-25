import requests
from datetime import datetime
import smtplib

myEmail = "ankushsmtp401@gmail.com"
password = "whxo fuzg kyhv ftzx"

MY_LAT = 21.146633 #atitude
MY_LONG = 79.088860 #longitude

def isISSOverhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


#Your position is within +5 or -5 degrees of the ISS position.

def isNight():
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

    if time_now >= sunset or time_now<= sunrise:
        return True

if isISSOverhead() and isNight():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(myEmail,password)
    connection.sendmail(
        from_addr=myEmail,
        to_addrs=myEmail,
        msg="Subject:Look Up \n\nThe iss is right above you."
    )


