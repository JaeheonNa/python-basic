import turtle

pen = turtle.Pen()
flag = True

while flag :
    direction = input("왼쪽=left, 오른쪽=right, 종료=quit : ")

    if direction == "right" :
        pen.right(45)

    if direction == "left" :
        pen.left(45)

    if direction == "quit" :
        flag = False

    pen.forward(100)

turtle.exitonclick() # 터틀 그래픽 창이 클릭 돼야 창이 꺼지도록 하는 코드