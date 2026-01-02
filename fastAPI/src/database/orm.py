from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

from schema.request import CreateToDoRequest


Base = declarative_base()


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True, index=True)
    contents = Column(String(256), nullable=False)
    is_done = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("user.id"))

    def __repr__(self):
        return f"Todo(id={self.id}, contents={self.contents}, is_done={self.is_done})"

    @classmethod
    def create(cls, request: CreateToDoRequest):
        return cls(contents=request.contents, is_done=request.is_done)

    def done(self) -> "Todo":
        self.is_done = True
        return self

    def undone(self) -> "Todo":
        self.is_done = False
        return self


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(256), nullable=False)
    password = Column(String(256), nullable=False)
    # email = Column(String(256), nullable=True)

    # 가상의 관계만 생성. OneToMany와 같음. User select 시 Todo가 left outer join 돼서 반환 됨.
    # Lazy Loading: 연관된 객체가 실제로 필요할 때 조회. 단, 반복문에서 돌릴 때, 그 때마다 쿼리를 돌림.(N+1)
    # Eager Loading: 데이터를 조회할 때 처음부터 연관된 객체를 조인하여 읽어옴. N+1 문제는 발생하지 않지만, 꼭 필요하지 않은 데이터까지 join해서 읽어올 수 있음.
    # lazy="joined": eager loading
    # lazy="select": lazy loading (default)
    todos = relationship("Todo", lazy="joined")

    @classmethod
    def create(cls, username: str, hashed_password: str):
        return cls(username=username, password=hashed_password)
