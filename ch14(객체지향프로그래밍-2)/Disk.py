class Disk(object):
    def __init__(self, capa, rpm):
        self.__capa = capa
        self.__rpm = rpm

    def getCapa(self):
        return self.__capa
    def setCapa(self, capa):
        self.__capa = capa

    def getRpm(self):
        return self.__rpm
    def setRpm(self, rpm):
        self.__rpm = rpm

    def __str__(self):
        return "Disk Capacity: %sGB \nRPM: %s" % (str(self.getCapa()), str(self.getRpm()))