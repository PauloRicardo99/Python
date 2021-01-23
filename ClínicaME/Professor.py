import Funcionario as funcionario

class Professor(funcionario.Funcionario):
    def __init__(self):
        super().__init__()
        self.formacao = ""
        self.disciplina = ""

    def cadastrarProfessor(self):
        super().cadastrarFuncionario()
        self.formacao = str(input("Formação: "))
        self.disciplina = str(input("Disciplina: "))

    def exibirProfessor(self):
        super().exibirFuncionario()
        print(self.formacao)
        print(self.disciplina)