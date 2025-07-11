import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_list_tasks_empty():
    resp = client.get("/tasks")
    assert resp.status_code == 200
    assert resp.json() == []

def test_create_task_and_score():
    # Crea una tarea de ejemplo
    payload = {
        "title":"Test",
        "description":"Desc",
        "city":"Quito",
        "temp_min":15,
        "temp_max":25,
        "rain":False,
        "wind":5
    }
    r1 = client.post("/tasks", json=payload)
    assert r1.status_code == 200
    # Comprueba que aparece en lista
    r2 = client.get("/tasks")
    assert r2.status_code == 200
    assert len(r2.json()) == 1

    # Ahora prueba el endpoint de score
    score_payload = {
        "prefs": {"temp_min":15,"temp_max":25,"rain":False,"wind":5},
        "weather": {"temp":20,"wind":3,"condition":"Clear"}
    }
    r3 = client.post("/tasks/score", json=score_payload)
    assert r3.status_code == 200
    assert "score" in r3.json()
    assert isinstance(r3.json()["score"], int)
