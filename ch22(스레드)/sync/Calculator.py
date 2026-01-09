import time
import threading

lock = threading.Lock()

class Calculator():

    def __init__(self, memory):
        super().__init__()
        self.memory = memory

    def getMemory(self):
        return self.memory

    def setMemory(self, memory):
        lock.acquire()
        self.memory = memory
        time.sleep(1)
        print(threading.current_thread().name, ":", self.memory)
        lock.release()
