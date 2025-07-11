from fastapi import FastAPI
from app.services.weather import get_weather_for_city
from app.services.score import calculate_score
from typing import Dict

from pydantic import BaseModel
app = FastAPI()

class Task(BaseModel):
    title: str
    description: str
    city: str
    temp_min: float
    temp_max: float
    rain: bool
    wind: float

tasks = []

@app.get("/tasks")
def list_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.get("/weather/{city}")
def weather_city(city: str):
    """
    Devuelve datos de clima formateados para la ciudad indicada.
    """
    data = get_weather_for_city(city)
    return {
        "city": city,
        "weather": {
            "temp": data["main"]["temp"],
            "wind": data["wind"]["speed"],
            "condition": data["weather"][0]["main"]
        }
    }

@app.post("/tasks/score")
def score_task(payload: Dict):
    """
    Recibe payload con:
    {
      "prefs": {"temp_min":…, "temp_max":…, "rain":…, "wind":…},
      "weather": {"temp":…, "wind":…, "condition":…}
    }
    y devuelve {"score":…}
    """
    prefs = payload.get("prefs", {})
    weather = payload.get("weather", {})
    result = calculate_score(prefs, weather)
    return {"score": result}
