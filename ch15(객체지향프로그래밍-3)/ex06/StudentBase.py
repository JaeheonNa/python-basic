from abc import *

class StudentBase(metaclass=ABCMeta):

    @abstractmethod
    def study(self):
        pass

    @abstractmethod
    def goToSchool(self):
        pass