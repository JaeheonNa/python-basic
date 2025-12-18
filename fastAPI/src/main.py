from anyio.to_process import PosArgsT
from fastapi import FastAPI, Body, HTTPException
from pydantic import BaseModel

app = FastAPI()


todo_data = {
    1: {
        "id": 1,
        "contents" : "실전! FastAPI 섹선 0 수강",
        "is_done": True
    },
    2: {
        "id": 2,
        "contents" : "실전! FastAPI 섹선 1 수강",
        "is_done": False
    },
    3: {
        "id": 3,
        "contents" : "실전! FastAPI 섹선 2 수강",
        "is_done": False
    }
}

@app.get("/")
def health_check_handler():
    return {"ping": "pong"}

@app.get("/todos", status_code=200)
def get_todos_handler(order: str | None = None):
    todos = list(todo_data.values())
    if order and order == "DESC":
        return todos[::-1]
    return todos

@app.get("/todos/{todo_id}", status_code=200)
def get_todos_handler(todo_id: int):
    todo = todo_data.get(todo_id)
    if todo:
        return todo
    else:
        raise HTTPException(status_code=404, detail="ToDo not found")

class createToDoRequest(BaseModel):
    id: int
    contents: str
    is_done: bool

@app.post("/todos", status_code=201)
def create_todo_handler(request: createToDoRequest):
    todo_data[request.id] = request.dict()
    return todo_data[request.id]

@app.patch("/todos/{todo_id}", status_code=200)
def update_todo_handler(
    todo_id: int,
    # Body는 해당 필드가 requestBody에 담겨와야 함을 명시함. 반면 todo_id는 PathVariable이어서 이런 작업이 필요 없음.
    # ...은 해당 필드가 필수값이라는 뜻.
    # embed=True는 단일 필드를 json객체로 감싸서 받겠다는 의미.
    is_done: bool = Body(..., embed=True)
):
    todo = todo_data.get(todo_id)
    if todo:
        todo["is_done"] = is_done
        return todo
    else:
        raise HTTPException(status_code=404, detail="ToDo not found")

@app.delete("/todos/{todo_id}", status_code=204)
def delete_todo_handler(todo_id: int):
    todo = todo_data.pop(todo_id, None)
    if not todo:
        raise HTTPException(status_code=404, detail="ToDo not found")

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