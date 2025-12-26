from database.orm import Todo

def test_health_check(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert response.json() == {"ping" : "pong"}

#mocker 객체를 fixture로 받으려면, pytest-mock을 설치해야 함.
def test_get_todos(test_client, mocker):
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

def test_get_todo(test_client, mocker):
    #200
    mocker.patch("main.repository.get_todo_by_todo_id",
                 return_value=Todo(id=1, contents="todo", is_done=True)
    )
    response = test_client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "contents":"todo", "is_done": True}

    #404
    mocker.patch("main.repository.get_todo_by_todo_id", return_value=None)
    response = test_client.get("/todos/1")
    assert response.status_code == 404
    assert response.json() == {"detail":"ToDo not found"}
