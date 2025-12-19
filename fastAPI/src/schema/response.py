from typing import List

from pydantic import BaseModel

class TodoSchema(BaseModel):
    id: int
    contents: str
    is_done: bool

    # sqlalchemy의 orm 객체를 받아서 매핑해주는 설정.
    class Config:
        orm_mode = True

class TodoListSchema(BaseModel):
    todos: List[TodoSchema]