class Endereco():
    def __init__(self):
        self.logradouro = ""
        self.numero = ""
        self.complemento = ""
        self.cep = ""
        self.bairro = ""
        self.cidade = ""
        self.uf = ""
    def cadastrar_endereco(self):
        self.logradouro = input("Entre com o endereço: ")
        self.numero = input("Entre com o número: ")
        self.complemento = input("Entre com o complemento: ")
        self.cep = input("Entre com o cep: ")
        self.bairro = input("Entre com o bairro: ")
        self.cidade = input("Entre com a cidade: ")
        self.uf = input("Entre com o UF: ")
    def exibir_endereco(self):
        print(self.logradouro)
        print(self.numero)
        print(self.complemento)
        print(self.cep)
        print(self.bairro)
        print(self.cidade)
        print(self.uf)