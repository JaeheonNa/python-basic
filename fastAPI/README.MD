# 초기 세팅

### - project root dir에서 아래 명령어로 생성됨.

python3.11 -m venv fastAPI

### - 이후 fastAPI dir로 들어와서 아래 명령어로 가상환경 활성화를 해줘야 함.

source bin/activate

### - fastAPI를 설치한다 

pip install fastapi==0.97.0

### - uvicorn을 설치한다. fastapi를 동작시키기 위해 필요한 라이브러리다.

pip install uvicorn

### - main 파일이 있는 디렉토리로 이동 후 uvicorn을 이용해 fastapi를 구동한다.

(구동) uvicorn main:app   
(구동: 코드 변경 감지시 리로드) uvicorn main:app --reload 
(종료) Ctrl + c

### - 구동한 url에 /docs를 붙이면 swagger가 자동으로 생성된 걸 확인할 수 있다.

http://127.0.0.1:8000/docs

# DB 연결

### - 도커로 MySQL 구동. 패스워드 및 DB명 todos로 지정. todos란 이름의 볼륨을 생성해서 /db 디렉토리에 연결. docker container 명 todos로 지정. 이미지는 mysql:8.0

docker run -p 3306:3306 -e MYSQL_ROOT_PASSWORD=todos -e MYSQL_DATABASE=todos -d -v todos:/db --name todos mysql:8.0

### - sqlAlchemy: 관계형 DB를 사용하기 위한 Python 라이브러리

pip install sqlalchemy

### - pymysql: python과 mysql 을 연결해주는 라이브러리. Java의 jdbcConnector.

pip install pymysql

### - cryptography: pymysql을 통해 mysql에 연결할 때, 인증이나 암호 관련 처리를 해주는 라이브러리.

pip install cryptography

# TEST

### Test를 하는 라이브러리, pytest 설치

pip install pytest

### Test Client에서 내부적으로 사용하는 라이브러리 httpx 설치

pip install httpx


### python package 생성. '경로' 아님 주의!. package는 생성 시 __init__.py 파일이 생성됨. pytest는 파이썬 모듈인 경우에만 파일들을 테스트로 인지하고 코드를 실행함. 이 때 __init__.py가 있어야만 pytest가 정상적으로 경로를 탐색할 수 있음. 