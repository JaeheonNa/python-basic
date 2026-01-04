from typing import Optional

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from api import todo, user

app = FastAPI() # Singleton 'app'이라는 패턴으로 객체 생성.
app.include_router(todo.router)
app.include_router(user.router)

# 일종의 미들웨어. CSS, JPG, JS 파일 등을 staticFiles라고 함.
# app.mount("/static", StaticFiles(directory="static"), name="static")

# template이라는 디렉토리를 찾아 객체를 하나 생성.
templates = Jinja2Templates("templates")

# @app.get("/")
# def health_check_handler():
#     return {"ping": "pong"}

@app.get("/")
def health_check_handler(q: Optional[str] = "pong"):
    return {"ping": q}

# 응답을 할 때, HTMLResponse 타입으로 응답하는 API
@app.get("/book-e", response_class=HTMLResponse)
async def book_e_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "콜렉터 북북이"})

@app.get("/book-e/search", response_class=HTMLResponse)
async def book_e_search(request: Request, q: str):
    print(q)
    return templates.TemplateResponse("index.html", {"request": request, "title": "콜렉터 북북이", "keyword": q})
