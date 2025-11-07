from Vector2D import *

if __name__ == '__main__':
    vector1 = Vector2D(5, 2)
    vector2 = Vector2D(5, 3)
    vector3 = Vector2D(5, 4)
    vector_result4 = vector1 + vector2
    print(vector_result4)

    vector_result5 = vector1 - vector2
    print(vector_result5)

    vector_result6 = vector1 * vector3
    print(vector_result6)

    if (vector1 == vector3):
        print("vector1과 vector3는 논리적으로 동등한 인스턴스입니다.")
    else:
        print("vector1과 vector3는 논리적으로 동등하지 않은 인스턴스입니다.")