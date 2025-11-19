from Student import *
from Worker import *

class PartTimer(Student, Worker):

    def __init__(self):
        Student.__init__(self)
        Worker.__init__(self)
        print("나는 파트타임 근로자입니다.")

    def greeting(self):
        print("PartTimer 클래스의 greeting 메소드 호출됨.")