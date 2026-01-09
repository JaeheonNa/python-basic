class MyEnumerate():
    def __init__(self, str):
        self.str = str
        self.current = 0
        self.end = len(str)

    def __iter__(self):
        return self

    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        else:
            self.current += 1
            return (self.current - 1, self.str[self.current - 1])

