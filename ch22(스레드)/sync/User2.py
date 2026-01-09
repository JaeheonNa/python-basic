import threading

class User2(threading.Thread):
    def __init__(self):
        super().__init__()

    def setCalculator(self, calculator):
        self.calculator = calculator
        self.name = "User2"

    def run(self):
        self.calculator.setMemory(50)