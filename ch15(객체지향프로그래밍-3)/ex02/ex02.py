from PartTimer import *

if __name__ == '__main__':
    partTimer = PartTimer()
    partTimer.greeting() # 다이아몬드 상속. (Java에서는 허용되지 않음)
    print(PartTimer.__mro__)
