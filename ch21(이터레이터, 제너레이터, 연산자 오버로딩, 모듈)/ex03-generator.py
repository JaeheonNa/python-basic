# iterator vs generator
# iterator : 클래스를 반복 가능한 클래스로 만들어주며, 모든 로직을 수행한 후 한 번에 메모리에 데이터를 적제해서 출력.
# generator : Generator는 iterator의 특별한 형태로, yield 키워드를 사용. generator의 의미는 iterator을 생성하는 자라는 의미임.
#             Generator는 호출되면 자동으로 iterator 객체를 반환하며, 함수의 실행 상태를 유지하면서 필요할 때마다 값을 생성.
#             메모리 효율적이라는 점입니다. yield를 만나면 함수 실행이 일시정지되고, 다음 값이 요청될 때 중단된 지점부터 다시 실행됨.

def myGenerator(current, end):
    while current < end:
        yield current
        current += 1

if __name__ == '__main__':
    myIterator = myGenerator(1, 10)
    for x in myIterator:
        print(x, end=" ")
