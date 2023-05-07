# weather app

import requests

API_KEY = "YOUR_API_KEY_HERE"
CITY = "San Francisco"
UNITS = "metric"  # or "imperial" for Fahrenheit

url = f"http://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units={UNITS}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(f"Current temperature in {CITY}: {data['main']['temp']}°C")
else:
    print("Error fetching weather data")
