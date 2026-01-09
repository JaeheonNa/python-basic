class NumBox():
    def __init__(self, num):
        self.num = num

    def __add__(self, num):
        self.num += num
        return self

    def __radd__(self, num):
        self.num += num
        return self

    def __sub__(self, num):
        self.num -= num
        return self

    def __rsub__(self, num):
        self.num -= num
        return self

    def __str__(self):
        return str(self.num)