import ParticipanteReuniao as pr
import ParticipanteInterno as pi
import Ata as a
import os.path

pr = pr.ParticipanteReuniao()
pi = pi.ParticipanteInterno()
a = a.Ata()
rodando = True

while rodando == True:
    try:
        while True:
            menu = int(input(f"\n===================== Menu =====================\n"
                             f"[1] Menu Participantes\n"
                             f"[2] Menu Ata\n"
                             f"[3] Sair\n"))

            if menu == 1:
                menu = int(input(f"\n============== Menu Participantes ==============\n"
                                 f"[1] Cadastrar participante interno\n"
                                 f"[2] Cadastrar participante externo\n"
                                 f"[3] Apagar todos os participantes\n"
                                 f"[4] Exibir todos os participantes\n"
                                 f"[5] Voltar\n"))
                if menu == 1:
                    pr.CadastroPI()
                elif menu == 2:
                    pr.CadastroPE()
                elif menu == 3:
                    pr.Apagar()
                elif menu == 4:
                    pr.ExibirPI()
                    pr.ExibirPE()

            elif menu == 2:
                menu = int(input(f"\n=================== Menu Ata ===================\n"
                                 f"[1] Emitir ata\n"
                                 f"[2] Exibir ata\n"
                                 f"[3] Sugestão\n"
                                 f"[4] Salvar\n"
                                 f"[5] Concluir a ata\n"
                                 f"[6] Voltar\n"))

                if menu == 1:
                    pi.verificar_emissor()
                    if pi.cont == 1:
                        a.emitir()
                    else:
                        print("Não há um emissor cadastrado.")

                elif menu == 2:
                    a.exibir()

                elif menu == 3:
                    pi.verificar_emissor()
                    if pi.cont == 1:
                        print("\n===============O emissor concorda?===============")
                        a = str(input("S/N\n"))
                        if a == 'S' or a == 's':
                            a.emitir()
                    else:
                        print("Não há um emissor cadastrado.")

                elif menu == 4:
                    a.salvar()

                elif menu == 5:
                    a.concluir()


            elif menu == 3:
                rodando = False
                break


    except ValueError:
        print('A opção inserida é inválida!')