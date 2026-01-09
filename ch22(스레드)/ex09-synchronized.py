from sync.Account import *
from sync.WithdrawThread1 import *
from sync.WithdrawThread2 import *

if __name__ == '__main__':
    account = Account(0)
    mother = WithdrawThread1()
    mother.setAccount(account)
    son = WithdrawThread2()
    son.setAccount(account)

    mother.start()
    time.sleep(1)
    son.start()


