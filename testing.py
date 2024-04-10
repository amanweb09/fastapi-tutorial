"""
For testing we need to install httpx
pip install httpx
"""
from fastapi.testclient import TestClient
from .main import app

client = TestClient(app)

def test_home():
    res = client.get("/")
    assert res.status_code == 200
    assert res.json() == {"message": "Welcome to Home"}