import time

# yield from 을 쓰면 yield를 쓸 때와 달리, 대기상태로 빠지지 않고, iterator처럼 데이터를 모두 메모리에 적재함.
def myGenerator():
    list1 = [10, 20, 30, 40, 50]
    yield from list1

if __name__ == '__main__':
    myIterator = myGenerator()
    for x in myIterator:
        print(x, end=' ')