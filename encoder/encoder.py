from abc import ABC, abstractmethod

class Encoder(ABC): 

    @abstractmethod
    def encode(sentence):
        pass
    
    @abstractmethod
    def getSimilarity(sentence):
        pass

    