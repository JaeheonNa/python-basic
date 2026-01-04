from fastapi import FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

router = APIRouter(prefix="/book-e")

# template이라는 디렉토리를 찾아 객체를 하나 생성.
templates = Jinja2Templates("templates")

# 응답을 할 때, HTMLResponse 타입으로 응답하는 API
@router.get("/book-e", response_class=HTMLResponse)
async def book_e_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "title": "콜렉터 북북이"})

@router.get("/book-e/search", response_class=HTMLResponse)
async def book_e_search(request: Request, q: str):
    print(q)
    return templates.TemplateResponse("index.html", {"request": request, "title": "콜렉터 북북이", "keyword": q})