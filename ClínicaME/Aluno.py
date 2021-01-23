import Pessoa as p

class Aluno(p.Pessoa):
    def __init__(self):
        super().__init__()
        self.codigo = 0
        self.interesse = ""
        self.celular = ""
        self.email = ""

    def cadastrarAluno(self):
        super().cadastrarPessoa()
        self.codigo = int(input("Código: "))
        self.interesse = input("Interesse: ")
        self.celular = input("Celular: ")
        self.email = int(input("Email: "))

    def exibirAluno(self):
        super().exibirPessoa()
        print(self.codigo)
        print(self.interesse)
        print(self.celular)
        print(self.email)