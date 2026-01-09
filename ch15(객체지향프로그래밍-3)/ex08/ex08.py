from Tank import *
from DropShip import *
from Marine import *

if __name__ == '__main__':

    tank1 = Tank()
    tank1.stop("탱크", 0, 0)
    dropShip1 = DropShip()
    dropShip1.stop("드랍쉽", 0, 0)
    marine1 = Marine()
    marine1.stop("마린", 0, 0)
    dropShip1.load(tank1)
    dropShip1.load(marine1)

    dropShip1.unload()
    dropShip1.unload()

    marine1.stimPack()
    marine1.move(10, 30)

    tank1.move(10, 30)
    tank1.siegeMode()
    tank1.moveMode()