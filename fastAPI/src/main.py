from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles

from api import todo, user, book_e
from database.mongo_connection import mongo_db

app = FastAPI()  # Singleton 'app'이라는 패턴으로 객체 생성.
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


# 서버가 처음 실행될 때 실행되는 함수
@app.on_event("startup")
def on_app_startup():
    mongo_db.connect()
    print("Connected to MongoDB")


# 서버가 종료될 때 실행되는 함수
@app.on_event("shutdown")
def on_app_shutdown():
    mongo_db.disconnect()
    print("Disconnected to MongoDB")
