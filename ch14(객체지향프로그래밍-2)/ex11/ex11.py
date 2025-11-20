from Rectangle import *

def onScreenClick(x, y):
    rect = Rectangle(x, y)
    rect.drawShape()

if __name__ == '__main__':
    screen = turtle.Screen()
    screen.setup(width=600, height=600)
    screen.title("마우스 왼쪽 클릭 시 사각형 그리기")
    turtle.onscreenclick(onScreenClick, 1)
    turtle.done()