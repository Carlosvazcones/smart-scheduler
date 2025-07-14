import pytest
from app.services.score import calculate_score

@pytest.mark.parametrize("prefs, weather, expected", [
    ({"temp_min":15,"temp_max":25,"rain":False,"wind":5}, {"temp":20,"wind":3,"condition":"Clear"}, 100),
    ({"temp_min":15,"temp_max":25,"rain":False,"wind":5}, {"temp":10,"wind":3,"condition":"Clear"}, 90),
    ({"temp_min":15,"temp_max":25,"rain":False,"wind":5}, {"temp":30,"wind":3,"condition":"Clear"}, 80),
    ({"temp_min":15,"temp_max":25,"rain":False,"wind":5}, {"temp":20,"wind":6,"condition":"Clear"}, 95),
    ({"temp_min":15,"temp_max":25,"rain":False,"wind":5}, {"temp":20,"wind":3,"condition":"Rain"}, 70),
])
def test_calculate_score(prefs, weather, expected):
    score = calculate_score(prefs, weather)
    assert score == expected
