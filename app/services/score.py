from typing import Dict

def calculate_score(
    prefs: Dict,     # ej. {"temp_min":15, "temp_max":25, "rain":False, "wind":5}
    weather: Dict    # ej. {"temp":20, "wind":3, "condition":"Clear"}
) -> int:
    """
    Calcula un puntaje de 0 a 100 según desviación entre preferencias y clima actual.
    """
    score = 100

    # Temperatura
    temp = weather.get("temp", 0)
    if temp < prefs["temp_min"]:
        score -= int((prefs["temp_min"] - temp) * 2)  # 2 puntos por grado bajo
    if temp > prefs["temp_max"]:
        score -= int((temp - prefs["temp_max"]) * 2)  # 2 puntos por grado alto

    # Lluvia
    if weather.get("condition").lower().find("rain") != -1 and not prefs["rain"]:
        score -= 30

    # Viento
    if weather.get("wind", 0) > prefs["wind"]:
        score -= int((weather["wind"] - prefs["wind"]) * 5)  # 5 puntos por m/s extra

    # Entre 0 y 100
    return max(0, min(100, score))
