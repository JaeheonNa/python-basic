from Disk import *

class HDD(Disk):

    def __init__(self, capa, rpm):
        super().__init__(capa, rpm)
        self.__capa = capa
        self.__rpm = rpm

    def __str__(self):
        return "HDD Capacity: %sGB \nRPM: %s" % (str(self.getCapa()), str(self.getRpm()))
