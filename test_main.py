from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    r = client.get("/")
    assert r.status_code == 200


def test_positive_text():
    r = client.post("/predict", json={"text": "I love this"})
    assert r.status_code == 200
    assert r.json()["sentiment"] == "POSITIVE"


def test_negative_text():
    r = client.post("/predict", json={"text": "This was terrible"})
    assert r.status_code == 200
    assert r.json()["sentiment"] == "NEGATIVE"


def test_missing_text():
    r = client.post("/predict", json={})
    assert r.status_code == 422


def test_history():
    r = client.get("/history")
    assert r.status_code == 200
    assert isinstance(r.json(), list)