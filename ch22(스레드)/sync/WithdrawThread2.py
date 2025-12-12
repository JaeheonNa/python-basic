import threading

class WithdrawThread2(threading.Thread):
    def __init__(self):
        super().__init__()
        self.account = None

    def setAccount(self, account):
        self.account = account
        self.name = '아들'

    def run(self):
            self.account.withdraw(300)
    