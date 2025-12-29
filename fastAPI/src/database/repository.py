from typing import List

from fastapi import Depends
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from database.orm import Todo, User
from database.connection import get_db


class TodoRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def get_todos(self) -> List[Todo]:
        return list(self.session.scalars(select(Todo)))

    def get_todo_by_todo_id(self, todo_id: int) -> Todo | None:
        return self.session.scalar(select(Todo).where(Todo.id == todo_id))

    def create_todo(self, todo: Todo):
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def update_todo(self, todo: Todo):
        self.session.add(todo)
        self.session.commit()
        self.session.refresh(todo)
        return todo

    def delete_todo(self, todo_id: int):
        self.session.execute(delete(Todo).where(Todo.id == todo_id))
        self.session.commit()


class UserRepository:
    def __init__(self, session: Session = Depends(get_db)):
        self.session = session

    def create_user(self, user: User):
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_user_by_username(self, username: str) -> User | None:
        return self.session.scalar(select(User).where(User.username == username))
