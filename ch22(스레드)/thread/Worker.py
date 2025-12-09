import threading
import time

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("작업 스레드 시작: ", threading.current_thread().name)
        time.sleep(3)
        print("작업 스레드 종료: ", threading.current_thread().name)
