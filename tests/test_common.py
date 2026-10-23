from src.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


class TestCommnon:
    def test_read_root(self) -> None:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "Hello World"}

    def test_read_health(self) -> None:
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "ok"}
