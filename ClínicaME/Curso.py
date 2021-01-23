import Professor as p

class Curso():
    def __init__(self):
        self.titulo = ""
        self.descricao = ""
        self.valor = 0.0
        self.professor = p.Professor()

    def cadastrar_curso(self):
        self.titulo = input("Curso: ")
        self.descricao = input("Descrição: ")
        self.valor = float(input("Valor: "))

    def calcular_min_aluno(self, salario=0.0):
        return self.valor/salario

    def exibir_curso(self):
        print(self.titulo)
        print(self.descricao)
        print(self.valor)
        print("Valor mínimo do curso: {}".format(calcular_min_aluno(4000.00)))


