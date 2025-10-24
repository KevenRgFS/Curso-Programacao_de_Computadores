from Pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, idade, CPF, matricula, curso, semestre):
        super().__init__(nome, idade, CPF)
        self.matricula = matricula
        self.curso = curso
        self.semestre = semestre

    def descricao(self):

        print("Informações do Aluno:\n")
        print(f"Nome: {self.nome}")
        print(f"Matrícula: {self.matricula}")
        print(f"Curso: {self.curso}")
        print(f"Semestre: {self.semestre}\n")



