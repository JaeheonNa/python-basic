from unsync.CounterThread import *

if __name__ == '__main__':

    for _ in range(4):
        thread = CounterThread()
        thread.start()

    print("모든 스레드들이 종료될 때까지 기다립니다.")
    mainThread = threading.current_thread()
    for thread in threading.enumerate(): # threading.enumerate() : 현재 active한 thread를 리스트로 반환함.
        if thread.name is not mainThread.name:
            thread.join()

    totalCount = format(CounterThread().getTotalCount(), ',')
    print("totalCount: ", totalCount)
    print("메인 스레드가 종로됩니다.")