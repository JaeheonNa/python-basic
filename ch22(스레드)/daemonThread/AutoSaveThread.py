import threading
import time

class AutoSaveThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            time.sleep(1)
            self.save()

    def save(self):
        print("작업내용 저장됨!")

