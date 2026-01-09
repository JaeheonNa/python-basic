from Person import *

class Student(Person):

    def __init__(self):
        Person.__init__(self)
        print("나는 학생입니다.")

    def greeting(self):
        print("Student 클래스의 greeting 메소드 호출됨.")