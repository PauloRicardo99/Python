import os
import docente as d
import secretaria as s

class menuCadastro():
    docente = d.docente()
    secretaria = s.secretaria()
    #def __init__(self):
        
    def exibir(self):
        while True :
            os.system('cls' if os.name == 'nt' else 'clear')
            print('-'*40)
            print('''Menu :
            [1]-Cadastrar um Docente
            [2]-Cadastrar um Secretaria
            [3]-Sair
            ''')
            menu=(int(input('opção desejada: ')))
            if menu==3:
                break
            elif menu==1:
                self.docente.cadastrar()
                os.system('cls' if os.name == 'nt' else 'clear')
            elif menu==2:
                self.secretaria.cadastrar()
                input('Pressione enter para voltar')
                os.system('cls' if os.name == 'nt' else 'clear')
            