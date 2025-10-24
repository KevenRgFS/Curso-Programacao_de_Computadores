from abc import ABC, abstractmethod

class Pessoa(ABC):

    def __init__(self, nome, idade, CPF):

        self.nome = nome
        self.idade = idade
        self.CPF = CPF

    @abstractmethod
    def descricao(self):
        pass
        


    
