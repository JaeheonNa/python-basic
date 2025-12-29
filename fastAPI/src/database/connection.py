from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:todos@localhost:3306/todos"


engine = create_engine(DATABASE_URL, echo=True)  # echo=True: SQL을 로그로 찍는 옵션
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    session = SessionFactory()
    try:
        # yield를 하고 나면, 여기에 의존해 있는 함수가 끝나야 그 다음 코드로 넘어감.
        # 즉 yield는 함수를 중간에 멈춰놓는 키워드.
        yield session
    finally:
        session.close()
