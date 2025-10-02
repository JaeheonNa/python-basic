from random import *

# randint(start, end) -> start부터 end까지의 정수 중 하나를 무작위로 뽑음.
print(randint(1, 6))

# random() -> 0이상 1미만의 실수 중 하나를 무작위로 뽑음.
print(random())

# randrange(start, end, step) -> start부터 end까지의 정수 중 step 단위로 떨어진 수 하나를 무작위로 뽑음.
print(randrange(1, 100, 2))

# randrange(end) -> 0부터 end미만까지의 정수 중 하나를 무작위로 뽑음.
print(randrange(10))

dice_num = randint(1, 6)
if dice_num == 1:
    num = 1
elif dice_num == 2:
    num = 2
elif dice_num == 3:
    num = 3
elif dice_num == 4:
    num = 4
elif dice_num == 5:
    num = 5
else:
    num = 6

print("주사위 눈: ", num)