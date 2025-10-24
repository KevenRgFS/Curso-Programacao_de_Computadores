from Pessoa import Pessoa

class Professor(Pessoa):

    def __init__(self, nome, idade, CPF, materias, cursos):
        super().__init__(nome, idade, CPF)
        self.materias = materias
        self.cursos = cursos

    def descricao(self):

        print("Informações do Docente:\n")
        print(f"Nome: {self.nome}")
        print(f"Matéria: {self.materias}")
        print(f"Cursos: {self.cursos}\n")
        
