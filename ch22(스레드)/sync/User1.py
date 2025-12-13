import threading

class User1(threading.Thread):
    def __init__(self):
        super().__init__()

    def setCalculator(self, calculator):
        self.calculator = calculator
        self.name = "User1"

    def run(self):
        self.calculator.setMemory(100)