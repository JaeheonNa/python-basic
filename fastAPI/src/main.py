from fastapi import FastAPI, Body, HTTPException, Depends
from pydantic import BaseModel

from database import repository
from database.connection import *
from sqlalchemy.orm import Session
from typing import List
from database.orm import Todo
from schema.request import CreateToDoRequest
from schema.response import TodoSchema, TodoListSchema

app = FastAPI()

@app.get("/")
def health_check_handler():
    return {"ping":"pong"}

@app.get("/todos", status_code=200)
def get_todos_handler(
    order: str | None = None,
    session: Session = Depends(get_db)
):

    todos: List[Todo] = repository.get_todos(session)

    if order and order == "DESC":
        todos = todos[::-1]

    return TodoListSchema(
        todos=[TodoSchema.model_validate(todo) for todo in todos]
    )

@app.get("/todos/{todo_id}", status_code=200)
def get_todos_handler(
    todo_id: int,
    session: Session = Depends(get_db)
):
    todo: Todo | None = repository.get_todo_by_todo_id(session, todo_id)
    if todo:
        return TodoSchema.model_validate(todo)
    else:
        raise HTTPException(status_code=404, detail="ToDo not found")

@app.post("/todos", status_code=201)
def create_todo_handler(
    request: CreateToDoRequest,
    session: Session  = Depends(get_db)
) -> TodoSchema | None:
    todo: Todo = Todo.create(request=request)
    todo: Todo = repository.create_todo(session=session, todo=todo)
    return TodoSchema.model_validate(todo)

@app.patch("/todos/{todo_id}", status_code=200)
def update_todo_handler(
    todo_id: int,
    # Body는 해당 필드가 requestBody에 담겨와야 함을 명시함. 반면 todo_id는 PathVariable이어서 이런 작업이 필요 없음.
    # ...은 해당 필드가 필수값이라는 뜻.
    # embed=True는 단일 필드를 json객체로 감싸서 받겠다는 의미.
    is_done: bool = Body(..., embed=True),
    session: Session = Depends(get_db)
):
    todo: Todo | None = repository.get_todo_by_todo_id(session, todo_id)
    if todo:
        todo.done() if is_done else todo.undone()
        todo: Todo = repository.update_todo(session, todo)
        return TodoSchema.model_validate(todo)
    else:
        raise HTTPException(status_code=404, detail="ToDo not found")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo_handler(
    todo_id: int,
    session: Session = Depends(get_db)
):
    todo: Todo = repository.get_todo_by_todo_id(session, todo_id)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")
    repository.delete_todo(session, todo_id)


# 요청 성공
# 200 OK            요청 성공, 범용적, GET/POST/PUT/PATCH
# 201 CREATE        요청 성공, 새로운 자원 생성, POST
# 204 NO CONTENT    요청 성공, 응답할 자원 없음, DELETE
#
# 요청 실패
# 400 BAD REQUEST   요청 실패, 요청이 잘못된 경우(query param, body)
# 401 UNAUTHORIZED  인증 실패
# 403 FORBIDDEN     권한 문제 또는 잘못된 method
# 404 NOT FOUND     자원이 없는 경우 또는 잘못된 endpoint
#
# 서버 에러
# 500 INTERNAL SERVER ERROR     범용적인 서버 에러
# 502 BAD GATEWAY               Reverse Proxy에서 서버의 응답을 처리할 수 없는 경우
# 503 SERVICE UNAVAILABLE       서버가 요청을 처리할 수 없는 경우