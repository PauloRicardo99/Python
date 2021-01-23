import funcionario as f
import folhaPagamento as fo


class docente(f.funcionario):
    def __init__(self):
        super().__init__()
        self.disciplina=""
        self.salario = fo.folhaPagamento()
        self.titulacao=""

    def cadastrar(self):

        self.disciplina=input("Disciplina: ")

        while True:
            self.titulacao=str(input("titulação: ")).upper()
            if self.titulacao == "MESTRE":
                self.salario.entrar_salario(4983.99)
                self.salario.calcular_folha()
                super().cadastrar()
                break
            elif self.titulacao == "DOUTOR":
                self.salario.entrar_salario(6423.57)
                self.salario.calcular_folha()
                super().cadastrar()
                break
            else:
                print('Títulação incorreta, Deseja corrigir ? S/N')
                a = str(input('')).upper()
                if a == 'N':
                    break

    def exibir(self):
        print(f'Disciplina: {self.disciplina}')       
        print(f'Titulação: {self.titulacao}')               
        super().exibir()
        self.salario.exibirFolhaPaga()

    def salvar(self):
        file = open('doecente.txt', 'a')
        file.write(f'Disciplina: {self.disciplina}') 
        file.write(f'Titulação: {self.titulacao}')
        file.write(f'{super().exibir()}')
        super().salvar(1)   
