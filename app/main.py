from fastapi import FastAPI
from app.services.weather import get_weather_for_city
from app.services.score import calculate_score

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
def task_score(task: Task):
    """
    Recibe la tarea (Task) y devuelve:
    { "task": Task, "score": int, "weather": {...} }
    """
    # Lógica de clima previa
    raw = get_weather_for_city(task.city)
    weather = {
        "temp": raw["main"]["temp"],
        "wind": raw["wind"]["speed"],
        "condition": raw["weather"][0]["main"]
    }
    prefs = {
        "temp_min": task.temp_min,
        "temp_max": task.temp_max,
        "allow_rain": task.rain,
        "max_wind": task.wind
    }
    sc = calculate_score(prefs, weather)
    return {"task": task, "score": sc, "weather": weather}
