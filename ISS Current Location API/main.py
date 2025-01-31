import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
#if response.status_code != 200:
#    raise Exception("Bad response from ISS API")
#
#if response.status_code == 404:
#    raise Exception("That resource does not exist.")
#elif response.status_code == 401:
#    raise Exception("You are not authorised to access this data.")
#=> Satırlarca if-elif açmak yerine aşağıdaki komutu kullanabiliriz.
response.raise_for_status()

data = response.json()  #["iss_position"]["longitude"]

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)

#=>LatLong sitesinden de bu değerleri girip görebilirsiniz.
