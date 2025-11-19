from Tiger import *
from Dog import *
from Cat import *

if __name__ == '__main__':
    ani1 = Animal("호돌이", 8, 180, Tiger())
    ani1.show()

    ani2 = Animal("바둑이", 4, 8, Dog())
    ani2.show()

    ani3 = Animal("미오", 3, 3, Cat())
    ani3.show()