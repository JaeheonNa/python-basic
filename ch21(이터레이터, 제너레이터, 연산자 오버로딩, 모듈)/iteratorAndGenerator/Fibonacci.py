class Fibonacci():
    def __init__(self, prev, current, end):
        self.prev = prev
        self.current = current
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        else:
            temp = self.current
            self.current += self.prev
            self.prev = temp
            return self.prev