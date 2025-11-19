class Buyer(object):
    money = 0
    bonusPoint = 0

    def buy(self, product):
        if self.money < product.price:
            print("잔액이 부족하여 물건 구입이 안 됩니다.")
            return
        else:
            self.money -= product.price
            self.bonusPoint += product.bonusPoint
            print(product, end = ' ')
            print("를 구매하셨습니다.")