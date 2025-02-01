import requests

parameters = {
    "amount": 10,
    "type": "boolean",
}

response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()  #4xx-5xx aralığındaki hata uyarıları verir.
data = response.json()
question_data = data["results"]
