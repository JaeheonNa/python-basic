import threading
import time

totalCount = 0

class CounterThread(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global totalCount

        for _ in range(2500000):
            temp = totalCount
            time.sleep(0)
            totalCount = temp + 1
        print(threading.current_thread().name, ": 2,500,000번 for문 동작")

    def getTotalCount(self):
        global totalCount
        return totalCount
