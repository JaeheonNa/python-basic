from overloading.Figure import *
from overloading.Quadrangle import *

quad = Quadrangle(2, 3)
figure = Figure(3, 4)
print("너비의 합: ", quad.width + figure.width)
print("높이의 합: ", quad.height + figure.height)