#import docente as d
import folhaPagamento as f

class funcionario(): 
    def __init__(self):
        self.matricula=0
        self.nome=""
        self.sexo=""
        self.nascimento=""
        #self.docente=d.docente()
        self.folhaPagamento= f.folhaPagamento()

    def cadastrar(self):
        self.matricula=int(input("matricula: "))
        self.nome=input("Nome: ")
        self.sexo=input("sexo: ")
        self.nascimento=input("nascimento: ")

    def exibir(self):
        print(f'Matrícula: {self.matricula}')
        print(f'Nome: {self.nome}')
        print(f'Sexo: {self.sexo}')
        print(f'Nascimento: {self.nascimento}')
        #self.docente.exibir()    

    def salvar(self, tipo):
        try:
            if tipo == 1:
                self.file = open('docente.txt', 'a')
            elif tipo == 2:
                self.file = open('secretaria.txt','a')
            elif tipo == 3:
                self.file = open('parecerista.txt', 'a')
            self.file.close()

        except Exception as erro:
            print(f"O problema do tipo {erro.__class__} encontrado no"
                  f"\nmétodo 'salvar' da classe 'Funcionário'.")