class protocolo():
    def __init__(self):
        self.dataEmissao=""
        self.dataInicioExp=""
        self.justificativaUsoAnimais=""
        self.resumoPt=""
        self.resumoEn=""
        self.dataEnvioParecer= ""
        self.dataEmissaoParecer=""
        self.statusProtocolo=""
        self.especie=""
        self.bioterio=""

    def emitir(self):
        self.dataEmissao=(input("Data Emissão: "))
        self.dataInicioExp=(input("Data do inicio do experimento: "))
        self.justificativaUsoAnimais=(input("Justificativa do uso de animais: "))
        self.resumoPt=(input("Resumo PT: "))
        self.resumoEn=(input("Resumo En: "))
        self.especie=(input("Especie: "))
        self.bioterio=(input("Bioterio: "))
        self.dataEnvioParecer= (input("Data de envio de parecer: "))

    def emitirParecer(self):
        self.dataEmissaoParecer=(input("Data de emissão do parecer: "))
        self.statusProtocolo=(input("status do protocolo: "))


    def exibir(self):
        print(f'\nData de emissão: {self.dataEmissao}')
        print(f'Data do início do experimento: {self.dataInicioExp}')
        print(f'Justificativa do uso de animais: {self.justificativaUsoAnimais}')
        print(f'Resumo em português: {self.resumoPt}')
        print(f'Resumo em inglês: {self.resumoEn}')
        print(f'Espécie: {self.especie}')
        print(f'Biotério: {self.bioterio}')
        print(f'Data de envio do parecer: {self.dataEnvioParecer}')

    def exibirParecer(self):
        print(f'\nData de emissão do parecer: {self.dataEmissaoParecer}')
        print(f'\nStatus do protocolo: {self.statusProtocolo}')

    def salvar(self):
        file = open('protocolo.txt', 'a')
        file.write('\n===========Protocolo==========\n')
        file.write(f'\nData de emissão: {self.dataEmissao}')
        file.write(f'\nData do início do experimento: {self.dataInicioExp}')
        file.write(f'\nJustificativa do uso de animais: {self.justificativaUsoAnimais}')
        file.write(f'\nResumo em português: {self.resumoPt}')
        file.write(f'\nResumo em inglês: {self.resumoEn}')
        file.write(f'\nEspécie: {self.especie}')
        file.write(f'\nBiotério: {self.bioterio}')
        file.write(f'\nData de envio do parecer: {self.dataEnvioParecer}\n')
        file.write('\n=====Parecer do Protocolo======\n')
        file.write(f'\nData de emissão do parecer: {self.dataEmissaoParecer}')
        file.write(f'\nStatus do protocolo: {self.statusProtocolo}\n')
        file.close

