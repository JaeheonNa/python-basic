import threading
import os

class Ping(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(threading.current_thread().name)
        for i in range(3):
            os.system('afplay /System/Library/Sounds/Ping.aiff')