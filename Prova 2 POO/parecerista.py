import docente as d

class parecerista(d.docente):
    def __init__(self):
        super().__init__()
        self.area=""

    def cadastrar(self):
        self.area=input("Area: ")
        super().cadastrar()


    def exibir(self):
        print('============Parecista===========')
        print(self.area)
        super().exibir()

    def salvar(self):
        file = open('parecerista.txt', 'a')
        file.write('============Parecista===========')
        file.write(self.area)
        file.write.super().exibir()
