### project root dir에서 아래 명령어로 생성됨.

python3.11 -m venv fastAPI

### 이후 fastAPI dir로 들어와서 아래 명령어로 가상환경 활성화를 해줘야 함.

source bin/activate

### fastAPI를 설치한다 

pip install fastapi==0.97.0

### uvicorn을 설치한다. fastapi를 동작시키기 위해 필요한 라이브러리다.

pip install uvicorn

### main 파일이 있는 디렉토리로 이동 후 uvicorn을 이용해 fastapi를 구동한다.

(구동) uvicorn main:app   
(구동: 코드 변경 감지시 리로드) uvicorn main:app --reload   
(종료) Ctrl + c

### 구동한 url에 /docs를 붙이면 swagger가 자동으로 생성된 걸 확인할 수 있다.

http://127.0.0.1:8000/docs