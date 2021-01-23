import Endereco as e

class Pessoa():
    def __init__(self):
        self.nome = ""
        self.rg = ""
        self.cpf = ""
        self.anoNasc = 0
        self.mesNasc = 0
        self.sexo = ""
        self.endereco = e.endereco()
    def cadastrar(self):
        self.nome = input("Entre com o nome: ")
        self.rg = input("Entre com o RG: ")
        self.cpf = input("Entre com o CPF: ")
        self.anoNasc = int(input("Entre com o ano de nascimento: "))
        self.mesNasc = int(input("Entre com o mês de nascimento: "))
        self.sexo = input("Informe o sexo:")
        self.endereco.cadastrar_endereco()
    def exibir(self):
        print(self.nome)
        print(self.rg)
        print(self.cpf)
        print(self.anoNasc)
        print(self.mesNasc)
        print(self.sexo)
        self.endereco.exibir_endereco()