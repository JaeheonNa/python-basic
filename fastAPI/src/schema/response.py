from typing import List
from pydantic import BaseModel, ConfigDict

class TodoSchema(BaseModel):
    id: int
    contents: str
    is_done: bool

    # sqlalchemy의 orm 객체를 받아서 매핑해주는 설정.
    model_config = ConfigDict(from_attributes=True)

class TodoListSchema(BaseModel):
    todos: List[TodoSchema]