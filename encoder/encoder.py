from abc import ABC, abstractmethod

class Encoder(ABC): 

    @abstractmethod
    def encode(sentence):
        pass
    
    @abstractmethod
    def most_similar(sentence):
        pass

    