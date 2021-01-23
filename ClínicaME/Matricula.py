import Curso as curso

class Matricula(curso.Curso):
    def __init__(self):
        super().__init__
        self.id = ""
        self.diaMatricula = ""
        self.mesMatricula = ""
        self.anoMatricula = ""
        self.nota = ""

    def matricularAluno(self):
        super().cadastrarCurso()
        self.id = int(input("ID: "))
        self.diaMatricula = int(input("Dia da matrícula: "))
        self.mesMatricula = str(input("Mês da matrícula: "))
        self.anoMatricula = int(input("Ano da matrícula: "))
        self.nota = float(input("Nota: "))

    def exibirMatricula(self):
        super().exibirCurso()
        print(self.id)
        print(self.diaMatricula)
        print(self.mesMatricula)
        print(self.anoMatricula)
        print(self.nota)
