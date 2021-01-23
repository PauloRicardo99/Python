import ParticipanteExterno as pe
import ParticipanteInterno as pi
import os.path

class ParticipanteReuniao():
    def __init__(self):
        self.ParticipanteExterno = pe.ParticipanteExterno()
        self.ParticipanteInterno = pi.ParticipanteInterno()

    def CadastroPE(self):
        while True:
            print("\n============= Participante externo =============")
            self.ParticipanteExterno.incluir()
            print("\n============== Verifique os dados ==============")
            self.ParticipanteExterno.exibir()
            print("\n=========== Os dados estão corretos? ===========")
            menu = str(input("S/N\n"))
            if menu == 'S' or menu == 's':
                self.ParticipanteExterno.salvar()
                break
            elif menu == 'N' or menu == 'n':
                print('\n====== Deseja inserir os dados novamente? ======')
                menu = str(input("S/N\n"))
                if menu == 'N' or menu == 'n':
                    break

    def CadastroPI(self):
        while True:
            print("\n==============Participante interno==============")
            self.ParticipanteInterno.incluir()
            print("\n===============Verifique os dados===============")
            self.ParticipanteInterno.exibir()
            print("\n============Os dados estão corretos?============")
            menu = str(input("S/N\n"))
            if menu == 'S' or menu == 's':
                self.ParticipanteInterno.verificar_emissor()
                if self.ParticipanteInterno.cont == 0:
                    print("\n===========O participante é o emissor?===========")
                    a = str(input("S/N\n"))
                    if a == 'S' or a == 's':
                        self.ParticipanteInterno.emissor = ''
                self.ParticipanteInterno.salvar()
                break
            elif menu == 'N' or menu == 'n':
                print('\n=======Deseja inserir os dados novamente?=======')
                menu = str(input("S/N\n"))
                if menu == 'N' or menu == 'n':
                    break

    def Apagar(self):
        print("\n================= Tem certeza? =================")
        menu = str(input("S/N\n"))
        if menu == 'S' or menu == 's':
            try:
                if os.path.exists('Participantes.txt'):
                    arquivo_part = open('Participantes.txt', 'w')
                    arquivo_part.close()

            except Exception as erro:
                print(f"O problema encontrado foi {erro.__class__}")

    def ExibirPI(self):
        print('\n')
        # Imprime todos os participantes internos
        cont = 10
        arquivo_part = open('Participantes.txt', 'r')
        for linha0 in arquivo_part:
            linha = linha0.strip()
            if linha == '==============Participante interno==============':
                cont = 0
            if cont < 9:
                print(linha)
                cont = cont + 1
        arquivo_part.close()

    def ExibirPE(self):
        # Imprime todos os participantes externos
        cont = 10
        arquivo_part = open('Participantes.txt', 'r')
        for linha0 in arquivo_part:
            linha = linha0.strip()
            if linha == '==============Participante externo==============':
                cont = 0
            if cont < 5:
                print(linha)
                cont = cont + 1
        arquivo_part.close()
        print('\n')