from database.orm import Todo
from database.repository import TodoRepository

#mocker 객체를 fixture로 받으려면, pytest-mock을 설치해야 함.
def test_get_todos(test_client, mocker):
    mocker.patch.object(TodoRepository, "get_todos", return_value=[
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
    mocker.patch.object(TodoRepository, "get_todo_by_todo_id",
                 return_value=Todo(id=1, contents="todo", is_done=True)
    )
    response = test_client.get("/todos/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "contents":"todo", "is_done": True}

    #404
    mocker.patch.object(TodoRepository, "get_todo_by_todo_id", return_value=None)
    response = test_client.get("/todos/1")
    assert response.status_code == 404
    assert response.json() == {"detail":"ToDo not found"}

def test_create_todo(test_client, mocker):
    create_spy = mocker.spy(Todo, "create") # Todo객체의 "create"라는 함수를 spy하겠다.
    mocker.patch.object(TodoRepository, "create_todo",
                 return_value=Todo(id=1, contents="todo", is_done=True))
    body = {
        "contents":"test",
        "is_done": False
    }
    response = test_client.post("/todos", json=body)

    # spy 객체를 이용한 검증
    assert create_spy.spy_return.id is None
    assert create_spy.spy_return.contents == "test"
    assert create_spy.spy_return.is_done is False

    assert response.status_code == 201
    assert response.json() == {
        "id":1, "contents":"todo", "is_done":True
    }

def test_update_todo(test_client, mocker):
    # 200
    undone = mocker.patch.object(Todo, "undone")
    mocker.patch.object(TodoRepository, "get_todo_by_todo_id",
                 return_value=Todo(id=1, contents="todo", is_done=True))
    mocker.patch.object(TodoRepository, "update_todo",
                 return_value=Todo(id=1, contents="todo", is_done=False))
    response = test_client.patch("todos/1", json={"is_done":False})

    undone.assert_called_once_with()
    assert response.status_code == 200
    assert response.json() == {"id": 1, "contents": "todo", "is_done": False}

    # 404
    mocker.patch.object(TodoRepository, "get_todo_by_todo_id", return_value=None)
    response = test_client.patch("todos/1", json={"is_done":True})
    assert response.status_code == 404
    assert response.json() == {"detail":"ToDo not found"}

def test_delete_todo(test_client, mocker):
    # 204
    mocker.patch.object(TodoRepository, "get_todo_by_todo_id",
                 return_value=Todo(id=1, contents="todo", is_done=True)
                 )
    mocker.patch.object(TodoRepository, "delete_todo", return_value=None)
    response = test_client.delete("/todos/1")
    assert response.status_code == 204

    # 404
    mocker.patch.object(TodoRepository, "get_todo_by_todo_id", return_value=None)
    response = test_client.delete("/todos/1")
    assert response.status_code == 404
    assert response.json() == {"detail": "ToDo not found"}