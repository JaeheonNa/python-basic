import random

# 정수 a ~ b 사이의 값
print("주사위의 눈:", random.randint(1, 6))
# 0.0 ~ 1.0 사이의 값
print("random():", random.random())
# a ~ b 사이의 값 중, a + c의 배수의 값.
print("randrange():", random.randrange(0, 101, 3))
# 리스트 내 요소 중 하나.
family = ["나루", "나솔", "나재헌", "문경진"]
print("choice():", random.choice(family))
# 리스트 순서를 섞음.
print("섞기 전:", family)
random.shuffle(family)
print("섞은 후:", family)
