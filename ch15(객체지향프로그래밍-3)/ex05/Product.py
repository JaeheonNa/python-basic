class Product(object):
    price = 0
    bonusPoint = 0

    def __init__(self, price):
        self.price = price
        self.bonusPoint = int(price * 0.1)