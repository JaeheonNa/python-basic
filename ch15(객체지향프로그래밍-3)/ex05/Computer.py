from Product import *

class Computer(Product):
    def __init__(self, price):
        super().__init__(price)

    def __str__(self):
        return "Computer"