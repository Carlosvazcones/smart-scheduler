import os
import requests
from typing import Dict

OPENWEATHER_API_KEY = "f7ad774adaf8dd30a0c96adea969d66e"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_for_city(city: str) -> Dict:
    """
    Llama a OpenWeatherMap y devuelve el JSON de la respuesta.
    """
    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric",
        "lang": "es"
    }
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    return response.json()
