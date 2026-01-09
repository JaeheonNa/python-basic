from Person import *
from University import *

class Undergraduate(Person, University):

    def __init__(self):
        Person.__init__(self)
        University.__init__(self)
        pass

    def study(self):
        print("공부합니다.")
