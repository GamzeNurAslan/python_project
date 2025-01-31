import requests
from datetime import datetime

MY_LAT = 38.674870
MY_LONG = 39.212399

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(sunrise.split("T"))

time_now = datetime.now()
print(time_now)
