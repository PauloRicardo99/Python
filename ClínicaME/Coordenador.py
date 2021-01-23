import Funcionario as funcionario

class Coordenador(funcionario.Funcionario):
    def __init__(self):
        super().__init__()
        self.area = ""
        self.plusSalario = ""

    def cadastrarCoordenador(self):
        super().cadastrarFuncionario()
        self.area = str(input("Área: "))
        self.plusSalario = str(input("Plus salário: "))

    def exibirCoordenador(self):
        super().exibirFuncionario()
        print(self.area)
        print(self.plusSalario)