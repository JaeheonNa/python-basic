from Tv import *
from Computer import *
from Audio import *
from Buyer import *

if __name__ == "__main__":
    buyer = Buyer()
    buyer.money = 1000
    tv = Tv(80)
    computer = Computer(50)
    audio = Audio(20)
    buyer.buy(tv)
    buyer.buy(computer)
    buyer.buy(audio)
    print("돈: ", buyer.money)
    print("보너스 포인트:", buyer.bonusPoint)
    buyer.buy(Computer(5000))
