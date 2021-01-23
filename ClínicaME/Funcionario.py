import Pessoa as p
import FolhaPagamento as fp

class funcionario(p.Pessoa):
    def __init__(self):
        super().__init__()
        self.matricula = 0
        self.setor = ""
        self.cargo = ""
        self.nivel = 0
        self.salario = 0.0
        self.folha = fp.calculo_folha()

    def cadastrar(self):
        self.matricula = int(input("Entre com a matricula: "))
        super().cadastrar()
        self.setor = input("Entre com o setor: ")
        self.cargo = input("Entre com o cargo: ")
        self.nivel = input("Entre com o nível: ")
        self.salario = float(input("Entre com o salário:"))
        self.folha.entrar_salario(self.salario)

    def exibir(self):
        print(self.matricula)
        super().exibir()
        print(self.setor)
        print(self.cargo)
        print(self.nivel)
        print(self.salario)
        self.folha.exibir_folha()