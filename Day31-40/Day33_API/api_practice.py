import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status
data = response.json()

iss_lat = float(data["iss_position"]["latitude"])
iss_lng = float(data["iss_position"]["longitude"])
print(data)
# print(response.status_code)