from ConcreteStudent2 import *

if __name__ == "__main__":
    student2 = ConcreteStudent2()
    student2.study()
    student2.goToSchool()

    # 추상 클래스의 용도: 추상 클래스를 상속 받는 각각의 자손 클래스에서 다른 내용으로 구현될 것을 예상하고 뼈대만 만드는 것.
    # 파이썬의 추상 클래스는 자바의 인터페이스와 같음.