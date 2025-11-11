class Account:
    __balance = 0

    def __init__(self):
        self.__balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("통장에 ", format(amount, ','), "원이 입금됨.")
            print("현재 잔액: ", format(self.getBalance(), ','), "원")

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            print("통장에 ", format(amount, ','), "원이 출금됨.")
            print("현재 잔액: ", format(self.getBalance(), ','), "원")

    def getBalance(self):
        return self.__balance