from pessoa import Pessoa

class Aluno(Pessoa):

    def __init__(self, nome, idade, CPF, matricula, curso, semestre, nota):
        super().__init__(nome, idade, CPF)
        self.matricula = matricula
        self.curso = curso
        self.semestre = semestre
        self.nota = nota

    @staticmethod
    def descricaoA():

        BusAlu = input("Qual aluno está procurando?\n")
        if BusAlu in alunos:
            print("\nInformações do aluno:\n")
            for chave, valor in alunos[BusAlu].items():
                print(f"{chave}: {valor}")
        else:
            print("Não foi encontrado nome correspondente!")
            return 0

    @staticmethod
    def AddA():

        print("\tIniciando Adição de novo Aluno\n")
        print("Declare as Informações abaixo:")
        nome = input("Nome Completo: ")
        idade = int(input("Idade: "))
        cpf = int(input("CPF: "))
        IDmatricula = int(input("Matricula de Identificação: "))
        matricula = "EFGa" + str(IDmatricula)
        curso = input("Curso: ")
        IDsemestre = int(input("Semestre: "))
        semestre = str(IDsemestre) + "°"

        
        alunos[nome] = {

        "Nome Completo": nome,
        "Idade": idade,
        "CPF": cpf,
        "Matrícula": matricula,
        "Curso": curso,
        "Semestre": semestre
        }

        print(f"\nAluno {nome} cadastrado!")

alunos = {

    "Lucas":
    {
        "Nome Completo": "Lucas Domingues",
        "Idade": 19,
        "CPF": 000000000000,
        "Matricula": "EFGa25106897",
        "Curso": "Ciencia da Computação",
        "Semestre": 2
    },

    "Lucas":
    {
        "Nome Completo": "Lucas Alexandre",
        "Idade": 18,
        "CPF": 000000000000,
        "Matricula": "EFGa25105489",
        "Curso": "Ciencia da Computação",
        "Semestre": 2
    }

    }



