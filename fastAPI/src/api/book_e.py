from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database.odm import BookModel
from database.mongo_connection import mongo_db

router = APIRouter(prefix="/book-e")

# template이라는 디렉토리를 찾아 객체를 하나 생성.
templates = Jinja2Templates("templates")


# 응답을 할 때, HTMLResponse 타입으로 응답하는 API
@router.get("/", response_class=HTMLResponse)
def get_book_e_index(request: Request):
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "콜렉터 북북이"}
    )


@router.get("/search", response_class=HTMLResponse)
def get_book_e_search(request: Request, q: str):
    print(q)
    return templates.TemplateResponse(
        "index.html", {"request": request, "title": "콜렉터 북북이", "keyword": q}
    )


@router.post("/", response_class=HTMLResponse)
async def create_book_e(request: Request):
    book = BookModel(keyword="파이썬", publisher="BJPublic", price=1200, image="me.png")
    await mongo_db.engine.save(book)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "콜렉터 북북이", "keyword": "파이썬"},
    )
