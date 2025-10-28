from pessoa import Pessoa
from notas import Nota

class Aluno(Pessoa):
    def __init__(self, nome, idade, CPF, matricula, curso, semestre):
        super().__init__(nome, idade, CPF)
        self.matricula = "EFGa" + matricula
        self.curso = curso
        self.semestre = semestre + "°"
        self.notas = Nota()

    def descricaoA(self):
        return f"Aluno: {self.nome} - Matrícula: {self.matricula} - Curso: {self.curso}"

    def dicionario(self):
        return {
            "nome": self.nome,
            "idade": self.idade,
            "CPF": self.CPF,
            "matricula": self.matricula,
            "curso": self.curso,
            "semestre": self.semestre,
            "notas": self.notas.dicionario()
        }

    @staticmethod
    def pegarDicio(d):
        a = Aluno(d.get("nome"), d.get("idade"), d.get("CPF"), d.get("matricula"), d.get("curso"), d.get("semestre"))
        if "notas" in d:
            a.notas.pegarDicio(d["notas"])
        return a
