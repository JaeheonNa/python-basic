from sync.User1 import *
from sync.User2 import *
from sync.Calculator import *

if __name__ == '__main__':
    calculator = Calculator(0)
    user1 = User1()
    user1.setCalculator(calculator)
    user2 = User2()
    user2.setCalculator(calculator)

    user1.start()
    user2.start()
    user1.join()
    user2.join()