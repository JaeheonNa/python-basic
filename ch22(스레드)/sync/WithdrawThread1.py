import threading

class WithdrawThread1(threading.Thread):
    def __init__(self):
        super().__init__()
        self.account = None

    def setAccount(self, account):
        self.account = account
        self.name = '어머니'

    def setBalance(self, amount):
        self.account.setBalance(amount)

    def run(self):
        self.account.setBalance(1000)
        self.account.withdraw(500)
        self.account.withdraw(300)
