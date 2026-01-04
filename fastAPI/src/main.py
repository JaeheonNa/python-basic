from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from api import todo, user, book_e

app = FastAPI() # Singleton 'app'이라는 패턴으로 객체 생성.
app.include_router(todo.router)
app.include_router(user.router)
app.include_router(book_e.router)

# 일종의 미들웨어. CSS, JPG, JS 파일 등을 staticFiles라고 함.
# app.mount("/static", StaticFiles(directory="static"), name="static")

# @app.get("/")
# def health_check_handler():
#     return {"ping": "pong"}

@app.get("/")
def health_check_handler(q: Optional[str] = "pong"):
    return {"ping": q}


