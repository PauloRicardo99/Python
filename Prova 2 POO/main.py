import funcionario as f 
import protocolo as p
import os
import menuCadastro as menu
import docente as d
import secretaria as s
import parecerista as pa

funcionario = f.funcionario()
protocolo = p.protocolo()
menuCadastro = menu.menuCadastro()
docente = d.docente()
secretaria = s.secretaria()
parecerista = pa.parecerista()
doc = False
sec = False
par = False
proto = False


try:
    while True :
        print('-'*40)
        print('''Menu :
[1]-Protocolo
[2]-Funcionário
[3]-Sair''')
        opc=(int(input('\n ')))
        if opc==5:
            break
        elif opc==1:
                print('''\nMenu :
[1]-Emitir Protocolo
[2]-Emitir Parecer
[3]-Exibir Protocolo
[4]-Exibir Parecer
[5]-Voltar''')
                menu = int(input(''))
                if menu == 1:
                    protocolo.emitir()
                    protocolo.salvar()
                    proto == True
                elif menu == 2:
                    if par == True and proto == True:
                        protocolo.emitirParecer()
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print('Nenhum Parecerista cadastrado ou protocolo emitido !')  
                        
                elif menu == 3:
                    if sec == True:
                        protocolo.exibir()
                        input('Pressione enter para voltar')
                        os.system('cls' if os.name == 'nt' else 'clear')
                    else:
                        print('Nenhuma Secretaria cadastrada !') 
                
                elif menu == 4:
                    if sec == True:
                        protocolo.exibirParecer()
                        input('Pressione enter para voltar')
                else:
                    print('Nenhuma Secretaria cadastrada !')              
                    os.system('cls' if os.name == 'nt' else 'clear')
            
        elif opc==2:
            print('''\n
[1] Cadastrar Docente
[2] Cadastrar Secretária
[3] Cadastrar Parecerista
[4] Exibir Funcionários
[5] Voltar''')
            menu = int(input(''))

            if menu == 1:
                docente.cadastrar()
                docente.salvar()
                doc = True
            elif menu == 2:
                secretaria.cadastrar()
                sec = True

            elif menu == 3:
                parecerista.cadastrar()
                par = True
            
            elif menu == 4:
                if doc == True:
                    print('============Docente============')
                    docente.exibir()
                if sec == True:
                    secretaria.exibir()
                if par == True:
                    parecerista.exibir ()   
                input('Pressione enter para voltar')
                os.system('cls' if os.name == 'nt' else 'clear')

        else:
            os.system('cls' if os.name == 'nt' else 'clear')    
            print('-'*40)
except ValueError:
    print('Opção Inválida!')        