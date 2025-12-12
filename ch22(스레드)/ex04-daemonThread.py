from thread.Worker import *

if __name__ == '__main__':
    print(threading.current_thread().name)
    worker_1 = Worker("worker-1")
    worker_1.daemon = True
    worker_1.start()
    print("메인스레드 종료됨.")