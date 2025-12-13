import threading

class ThreadVariable(threading.Thread):
    def __init__(self):
        super().__init__()
        self.lock = threading.Lock()
        self.lockValue = 0

    def plus(self, value):
        self.lock.acquire()
        self.lockValue += value
        self.lock.release()

    def getLockValue(self):
        return self.lockValue
