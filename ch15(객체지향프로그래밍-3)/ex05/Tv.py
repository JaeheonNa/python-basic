from Product import *

class Tv(Product):
    def __init__(self, price):
        super().__init__(price)

    def __str__(self):
        return "TV"