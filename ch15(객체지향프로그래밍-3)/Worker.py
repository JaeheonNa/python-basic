from Person2 import *

class Worker(Person2):

    def __init__(self):
        Person2.__init__(self)
        print("나는 근로자입니다.")

    def greeting(self):
        print("Worker 클래스의 greeting 메소드 호출됨.")