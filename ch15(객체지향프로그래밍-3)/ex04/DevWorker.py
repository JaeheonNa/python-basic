from SalesWorker import *

class DevWorker(SalesWorker):
    def __init__(self, name):
        super().__init__(name)
        self.name = name

    def work(self):
        print(self.name, "물건을 개발합니다.")