import funcionario as f
import folhaPagamento as fo

class secretaria(f.funcionario):
    def __init__(self):
        super().__init__()
        self.setor=""
        self.salario = fo.folhaPagamento()
        self.sal = 3533.80

    def cadastrar(self):
        self.setor=input("Setor: ")
        # self.salario=float(input("Salario: "))
        self.salario.entrar_salario(self.sal)
        self.salario.calcular_folha()
        super().cadastrar()
        self.salvar()
        super().salvar(2)


    def exibir(self):
        print('==========Secretária===========')
        print(f'\nSetor: {self.setor}')
        super().exibir()
        self.salario.exibirFolhaPaga()

    def salvar(self):
        try:
            file = open('secretaria.txt', 'a')
            file.write('\n==========Secretária===========')
            file.write(f'\nSetor: {self.setor}')
            file.write(f'\nSalário: {self.sal}')
            file.close()
        except Exception as erro:
            print(f'{erro.__class__}')