class folhaPagamento():
    def __init__(self):
        self.salario_bruto = 0.0
        self.inss = 0.0
        self.irrf = 0.0
        self.salario_liquido = 0.0
        self.salario_sem_inss = 0.0

    def entrar_salario(self, salario=0.0):
        self.salario_bruto = salario
    def calcular_inss(self):
        if self.salario_bruto < 1751.82:
            self.inss = self.salario_bruto * 0.08
        elif self.salario_bruto > 1751.81 and self.salario_bruto < 2919.73:
            self.inss = self.salario_bruto * 0.09
        elif self.salario_bruto > 2919.72 and self.salario_bruto < 5839.46:
            self.inss = self.salario_bruto * 0.11
        elif self.salario_bruto > 5839.45:
            self.inss = 817.66

    def calcular_irrf(self):
        self.irrf = self.salario_bruto * 0.15

    def calcular_folha(self):
        self.calcular_inss()
        self.calcular_irrf()
        self.salario_liquido = self.salario_bruto - (self.irrf + self.inss)

    def exibirFolhaPaga(self):
        print(f"\nSalario Bruto: R$ {self.salario_bruto}")
        print("-"*30)
        print("Descontos:")
        print(f"INSS: R$ {self.inss}")
        print(f"IRRF: R$ {self.irrf}")
        print("-"*30)
        print(f"Salario líquido: R$ {self.salario_liquido}")
        print("-"*30)
        