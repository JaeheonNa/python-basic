import time

def myUnlimitedRange():
    num = 0
    while True:
        yield num
        num += 1

if __name__ == '__main__':
    myRange = myUnlimitedRange()
    for num in myRange:
        print(num)
        time.sleep(0.5)