from fastapi.testclient import TestClient

from bee_ai.src.main import app


def test_root():
    client = TestClient(app)
    result = client.get("/")
    assert result.status_code == 200
    assert result.json() == {"message": "200"}
