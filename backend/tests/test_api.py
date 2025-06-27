from fastapi.testclient import TestClient
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
from main import app


client = TestClient(app)


def test_get_competitors():
    response = client.get("/competitors")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_times():
    response = client.get("/times")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
