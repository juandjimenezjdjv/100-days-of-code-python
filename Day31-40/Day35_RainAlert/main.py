import requests
import os
from twilio.rest import Client
from twilio.http.http_client import TwilioHttpClient

Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
your_key_API = os.environ.get("OWM_your_key_API")
account_sid = "Your account sid"
auth_token = os.environ.get("AUTH_TOKEN")

weather_params = {
    "lat": "Your lat",
    "lon": "Your long",
    "appid": your_key_API,
    "exclude": "current,minutely,daily"
}

response = requests.get(Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        rain = True

if rain:
    proxy_client = TwilioHttpClient()
    proxy_client.session.proxies = {'https': os.environ['https_proxy']}

    client = Client(account_sid, auth_token, http_client=proxy_client)
    message = client.messages \
        .create(
        body="It's going to rain today!!",
        from_="Your twilio virtual number",
        to="Your twilio virtual number"
    )
    print(message.status)
