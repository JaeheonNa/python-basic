from daemonThread.AutoSaveThread import *

if __name__ == '__main__':
    print("출력 결과")
    autoSaveThread = AutoSaveThread()
    autoSaveThread.daemon = True
    autoSaveThread.start()
    time.sleep(5)
    print("메인 스레드 종료됨")