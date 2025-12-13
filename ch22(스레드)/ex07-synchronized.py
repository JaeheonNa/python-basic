from sync.ThreadVariable import *
from sync.CounterThreadLock import *

if __name__ == '__main__':
    counterThreadLock = CounterThreadLock()
    counterThreadLock.setTotalCount(ThreadVariable())
    for _ in range(4):
        counterThreadLock = CounterThreadLock()
        counterThreadLock.start()

    print("모든 스레드들이 종료될 때까지 기다립니다.")
    mainThread = threading.current_thread()
    for thread in threading.enumerate():
        if thread.name is not mainThread.name:
            thread.join()

    print("totalCount: ", format(counterThreadLock.getTotalCount().getLockValue(), ','))