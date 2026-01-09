from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from database.odm import BookModel
from database.mongo_connection import mongo_db
from service.book import NaverBookScraper

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
async def get_book_e_search(request: Request, q: str):
    keyword = q.strip()
    if not keyword or len(keyword) == 0:
        context = {"request": request, "title": "콜렉터 북북이"}
        return templates.TemplateResponse("index.html", context)

    if await mongo_db.engine.find_one(BookModel, BookModel.keyword == keyword):
        books = await mongo_db.engine.find(BookModel, {"keyword": keyword})
        return templates.TemplateResponse(
            "index.html", {"request": request, "title": "콜렉터 북북이", "books": books}
        )

    naver_book_scraper = NaverBookScraper()
    books = await naver_book_scraper.search(keyword, 10, 5)
    bookModels = []
    for book in books:
        book_model = BookModel(
            keyword=keyword,
            publisher=book["publisher"],
            price=book["discount"],
            image=book["image"],
        )
        bookModels.append(book_model)
    await mongo_db.engine.save_all(bookModels)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "콜렉터 북북이", "books": bookModels},
    )


@router.post("/", response_class=HTMLResponse)
async def create_book_e(request: Request):
    # book = BookModel(keyword="파이썬", publisher="BJPublic", price=1200, image="me.png")
    # await mongo_db.engine.save(book)
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "title": "콜렉터 북북이", "keyword": "파이썬"},
    )
