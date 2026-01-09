from SalesWorker import *
from DevWorker import *

if __name__ == '__main__':
    worker1 = SalesWorker("데이브")
    worker2 = DevWorker("나재헌")

    worker1.work()
    worker2.work()