from typing import Dict

def calculate_score(
    prefs: Dict,     
    weather: Dict    
) -> int:
    """
    Calcula un puntaje de 0 a 100 según desviación entre preferencias y clima actual.
    """
    score = 100

    # Temperatura
    temp = weather.get("temp", 0)
    if temp < prefs["temp_min"]:
        score -= int((prefs["temp_min"] - temp) * 2)  
    if temp > prefs["temp_max"]:
        score -= int((temp - prefs["temp_max"]) * 4 )  

    # Lluvia
    if weather.get("condition").lower().find("rain") != -1 and not prefs["rain"]:
        score -= 30

    # Viento
    if weather.get("wind", 0) > prefs["wind"]:
        score -= int((weather["wind"] - prefs["wind"]) * 5)  

    # Entre 0 y 100
    return max(0, min(100, score))
