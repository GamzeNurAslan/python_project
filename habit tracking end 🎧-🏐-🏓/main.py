import requests
from datetime import datetime

USERNAME = "YOUR_NAME"
TOKEN = "YOUR_GRAPHS"
GRAPH_ID = "GRAPH_ID"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Write_Code Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

create_graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)

if create_graph_response.status_code == 200:
    print("Grafik başarıyla oluşturuldu!")
else:
    print(f"Grafik oluşturulurken bir hata oluştu: {create_graph_response.text}")

pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers did you cycle today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)

if response.status_code == 200:
    print("Pixel başarıyla eklendi!")
else:
    print(f"Pixel eklenirken bir hata oluştu: {response.text}")


update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
new_pixel_data = {
    "quantity": "4.5"
}

response_update = requests.put(url=update_endpoint, json=new_pixel_data, headers=headers)

if response_update.status_code == 200:
    print("Pixel başarıyla güncellendi!")
else:
    print(f"Pixel güncellenirken bir hata oluştu: {response_update.text}")

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
response_delete = requests.delete(url=delete_endpoint, headers=headers)

if response_delete.status_code == 200:
    print("Pixel başarıyla silindi!")
else:
    print(f"Pixel silinirken bir hata oluştu: {response_delete.text}")

#Pixela adlı bir platformu kullanarak kişisel verilerinizi izlemek için bir "cycling graph" (bisiklet sürüşü grafiği) 
#oluşturmayı ve bu grafiğe veri eklemeyi sağlar bu kod. Pixela, kullanıcıların günlük aktivitelerini (örneğin, yürüyüş, koşu, bisiklet sürme) takip etmelerini sağlayan bir platformdur.
