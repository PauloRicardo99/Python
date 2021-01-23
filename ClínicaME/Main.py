import Coordenador as coordenador
import Professor as professor
import Aluno as aluno

try:
    while True:
        cd = coordenador.Coordenador()
        pf = professor.Professor()
        al = aluno.Aluno()

        menu1 = int(input(f"[1] Coordenador\n[2] Professor\n[3] Aluno\n[4] Sair\n"))

        if menu1 == 1:
            print("\nCADASTRO\n==============================")
            cd.cadastrarCoordenador()
            print("\nEXIBIR\n==============================")
            cd.exibirCoordenador()
            print("\n")

        elif menu1 == 2:
            print("\nCADASTRO\n==============================")
            pf.cadastrarProfessor()
            print("\nEXIBIR\n==============================")
            pf.exibirProfessor()
            print("\n")

        elif menu1 == 3:
            print("\nCADASTRO\n==============================")
            al.cadastrarAluno()
            print("\nEXIBIR\n==============================")
            al.exibirAluno()
            print("\n")

        else:
            break

except ValueError:
    print("Entrada inválida!\n")