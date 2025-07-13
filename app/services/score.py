from typing import Dict

def calculate_score(preferences: Dict, weather: Dict) -> float:
    """
    preferences: { temp_min, temp_max, rain_ok (bool), wind_max }
    weather:     { temp, rain (bool), wind }
    Devuelve un puntaje entre 0 y 100.
    """
    score = 100.0

    # Temperatura: penaliza fuera de rango
    if weather["temp"] < preferences["temp_min"]:
        score -= (preferences["temp_min"] - weather["temp"]) * 2
    if weather["temp"] > preferences["temp_max"]:
        score -= (weather["temp"] - preferences["temp_max"]) * 2

    # Lluvia
    if not preferences["rain_ok"] and weather.get("rain", False):
        score -= 30

    # Viento
    if weather["wind"] > preferences["wind_max"]:
        score -= (weather["wind"] - preferences["wind_max"]) * 5

    return max(0.0, min(100.0, score))
