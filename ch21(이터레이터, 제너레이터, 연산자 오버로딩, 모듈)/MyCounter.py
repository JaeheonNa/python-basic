class MyCounter(object):

    def __init__(self, current, end):
        self.current = current
        self.end = end

    # Iterator 객체에서 반드시 구현해야할 메소드 1. __iter__
    def __iter__(self):
        return self

    # Iterator 객체에서 반드시 구현해야할 메소드 2. __next__
    def __next__(self):
        if self.current > self.end:
            # 현재 값이 마지막 값보다 크면 예외 발생.
            raise StopIteration
        else:
            # 현재 값을 그 다음 값으로 변경. 그리고 현재 값을 리턴.
            self.current += 1
            return self.current -1