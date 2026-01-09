import turtle

# 화면 설정
screen = turtle.Screen()
screen.setup(width=600, height=600)

# 거북이 생성
t = turtle.Pen()
t.shape("turtle")
t.forward(100)  # 움직임을 추가해서 확인
t.right(90)
t.forward(100)  # 움직임을 추가해서 확인
t.right(90)
t.forward(100)  # 움직임을 추가해서 확인
t.right(90)
t.forward(100)  # 움직임을 추가해서 확인
# 화면 유지
screen.exitonclick()