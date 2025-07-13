from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Dict
from app.services.weather import get_weather_for_city
from app.services.score import calculate_score

app = FastAPI()

# CORS configuration to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    title: str
    description: str
    city: str
    temp_min: float
    temp_max: float
    rain: bool
    wind: float

# In-memory storage for tasks
tasks: list[Task] = []

@app.get("/tasks")
def list_tasks() -> list[Task]:
    return tasks

@app.post("/tasks")
def create_task(task: Task) -> Task:
    tasks.append(task)
    return task

@app.get("/weather/{city}")
def weather_city(city: str) -> Dict:
    try:
        data = get_weather_for_city(city)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))
    return {
        "city": city,
        "weather": {
            "temp": data["main"]["temp"],
            "wind": data["wind"]["speed"],
            "condition": data["weather"][0]["main"]
        }
    }

@app.post("/tasks/score")
def score_task(task: Task) -> Dict:
    # 1) Fetch current weather
    try:
        data = get_weather_for_city(task.city)
    except Exception as e:
        raise HTTPException(status_code=502, detail=str(e))

    weather = {
        "temp": data["main"]["temp"],
        # Determine if it's raining based on weather description
        "rain": any(w.get('main', '').lower() in ['rain', 'drizzle'] for w in data["weather"]),
        "wind": data["wind"]["speed"]
    }

    # 2) Prepare preferences dict
    prefs = {
        "temp_min": task.temp_min,
        "temp_max": task.temp_max,
        "rain_ok": task.rain,
        "wind_max": task.wind
    }

    # 3) Calculate score
    try:
        score = calculate_score(prefs, weather)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating score: {e}")

    result = task.dict()
    result["score"] = score
    return result
