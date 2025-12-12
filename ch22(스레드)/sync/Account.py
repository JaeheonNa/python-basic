import threading
import time

class Account(threading.Thread):
    def __init__(self, balance):
        super().__init__()
        self.balance = balance
        self.lock = threading.Lock()

    def getBalance(self):
        return self.balance

    def setBalance(self, balance):
        self.lock.acquire()
        time.sleep(1)
        self.balance = balance
        print(threading.current_thread().name, "이/가 입금:", self.balance, "원")
        self.lock.release()

    def withdraw(self, amount):
        self.lock.acquire()
        time.sleep(2)
        self.balance -= amount
        if self.balance <= 0:
            try:
                print(threading.current_thread().name, "이/가", amount, "원 출금을 시도하였습니다.")
                raise Exception()
            except Exception:
                print("잔액이 부족합니다!")
        else:
            print(threading.current_thread().name, "이/가 출금:", amount, "원")
            print("통장 잔액: ", self.balance)
        self.lock.release()