from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome, idade, CPF, email=None, senha=""):
        super().__init__(nome, idade, CPF)
        self.email = email
        self.senha = senha  # armazenada em texto simples conforme solicitado

    def descricaoA(self):
        return f"Professor: {self.nome} - Email: {self.email}"

    def to_dict(self):
        return {"nome": self.nome, "idade": self.idade, "CPF": self.CPF, "email": self.email, "senha": self.senha}

    @staticmethod
    def from_dict(d):
        return Professor(d.get("nome"), d.get("idade"), d.get("CPF"), d.get("email"), d.get("senha", ""))
