from thread.Worker import *

if __name__ == "__main__":
    print("메인 스레드 시작")
    workers = []
    for i in range(5):
        name = "스레드->{}".format(i)
        worker = Worker(name)
        worker.start()
        workers.append(worker)

    for worker in workers:
        worker.join()

    print("메인 스레드 종료")

