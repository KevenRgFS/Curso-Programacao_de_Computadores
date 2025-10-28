from abc import ABC, abstractmethod

class Pessoa(ABC):
    def __init__(self, nome: str, idade: int, CPF: str):
        self.nome = nome
        self.idade = idade
        self.CPF = CPF

    @abstractmethod
    def descricaoA(self) -> str:
        raise NotImplementedError
