import turtle

pen = turtle.Pen()

for j in range(3):
    for i in range(4):
        pen.forward(100)
        pen.left(90)
    pen.right(20)


turtle.exitonclick()