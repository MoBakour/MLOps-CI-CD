from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_endpoint():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_predict_endpoint_returns_bucket_in_range():
    r = client.post("/predict", json={"user_id": "abc", "num_buckets": 10})
    assert r.status_code == 200
    data = r.json()
    assert "bucket" in data
    assert 0 <= data["bucket"] < 10
