from fastapi.testclient import TestClient

from main import app
from database.orm import Todo
from schema.response import TodoListSchema

## app(FastAPI) 객체를 대상으로 테스트를 수행할 객체 생성
test_client = TestClient(app=app)

def test_health_check():
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping" : "pong"}

def test_get_todos(mocker):
    mocker.patch("main.repository.get_todos", return_value=[
        Todo(id=1, contents="FastAPI Section 0", is_done=True),
        Todo(id=2, contents="FastAPI Section 1", is_done=False)
    ])
    response = test_client.get("/todos")
    assert response.status_code == 200
    assert response.json() == {
        "todos" : [
            {"id": 1, "contents":"FastAPI Section 0", "is_done": True},
            {"id": 2, "contents":"FastAPI Section 1", "is_done": False}
        ]
    }

    response = test_client.get("/todos?order=DESC")
    assert response.status_code == 200
    assert response.json() == {
        "todos": [
            {"id": 2, "contents": "FastAPI Section 1", "is_done": False},
            {"id": 1, "contents": "FastAPI Section 0", "is_done": True}
        ]
    }