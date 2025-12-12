import threading
import time

totalCount = None

class CounterThreadLock(threading.Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        global totalCount
        for _ in range(2500000):
            totalCount.plus(1)
        print(threading.current_thread().name, ": 2,500,000번 for문 동작")

    def getTotalCount(self):
        global totalCount
        return totalCount

    def setTotalCount(self, value):
        global totalCount
        totalCount = value
