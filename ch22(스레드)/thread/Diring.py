import threading
import os
import time


class Diring(threading.Thread):

    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print("띠링~")
        time.sleep(1)