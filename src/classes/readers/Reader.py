from abc import ABC, abstractclassmethod

class Reader(ABC):

    def __init__(self):
        self._pathname = ''
        self._elements = []

    @property
    def pathname(self):
        return self._pathname
    
    @pathname.setter
    def pathname(self, new_val):
        self._pathname = new_val

    @property
    def elements(self):
        return self._elements
    
    @elements.setter
    def elements(self, new_val):
        self._elements = new_val

    @abstractclassmethod
    def readFile(self):
        pass

    @abstractclassmethod
    def filterAttributes(self,attributes):
        pass