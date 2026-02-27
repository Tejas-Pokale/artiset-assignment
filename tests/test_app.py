from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_encode_decode():
    original = "DevOps Assignment"

    enc_response = client.post("/encrypt", data={"message": original})
    assert enc_response.status_code == 200

    encoded = enc_response.json()["result"]

    dec_response = client.post("/decrypt", data={"message": encoded})
    assert dec_response.status_code == 200

    decoded = dec_response.json()["result"]

    assert decoded == original