from fastapi.testclient import TestClient

from main import app

## app(FastAPI) 객체를 대상으로 테스트를 수행할 객체 생성
test_client = TestClient(app=app)

def test_health_check():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping" : "pong"}