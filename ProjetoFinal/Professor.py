from pessoa import Pessoa
from aluno import Aluno
from notas import Nota

class Professor(Pessoa):

    def __init__(self, nome, idade, CPF, materias, cursos):
        super().__init__(nome, idade, CPF)
        self.materias = materias
        self.cursos = cursos

    @staticmethod
    def descricaoA():

        BusPro = input("Qual professor está procurando?\n")
        if BusPro in professores:
            print("\nInformações do Professor:\n")
            for chave, valor in professores[BusPro].items():
                print(f"{chave}: {valor}")
        else:
            print("Não foi encontrado nome correspondente!")

    @staticmethod
    def AddA():

        print("\tIniciando Adição de novo professor\n")
        print("Declare as Informações abaixo:")
        nome = input("Nome Completo: ")
        idade = int(input("Idade: "))
        cpf = int(input("CPF: "))
        IDmatricula = int(input("Matricula de Identificação: "))
        matricula = "EFGp" + str(IDmatricula)
        materias = input("Matérias: ")

        
        professores[nome] = {

        "Nome Completo": nome,
        "Idade": idade,
        "CPF": cpf,
        "Matrícula": matricula,
        "Matérias": materias

        }

        print(f"\nAluno {nome} cadastrado!")

        def lancarNota():

            print("\tLançamento de Notas:\n")
            alu = input("Qual aluno terá sua nota alterada?\n")
            alu = Nota()

            Bim = int(input("Qual bimestre?\n"))

            

professores = {

    "Jessica":
    {
        "Nome Completo": "Jessica Oliveira",
        "Idade": 29,
        "CPF": 000000000000,
        "Matricula": "EFGp21137856",
        "Matéria": "Modelagem de Banco de Dados e UX"
    }

    }

