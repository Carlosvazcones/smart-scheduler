import os
import requests
from typing import Dict

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY", "TU_API_KEY_AQUÍ")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_for_city(city: str) -> Dict:
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "es"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
