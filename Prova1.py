from datetime import date

class Pessoa:
    def __init__(self):
        self.nome = ''
        self.datanasc = ''
        self.categoria = ''
        self.estado = ''
        self.aposentado = False
        self.valorbase = 0
        self.valorfinal = 0
        self.numerofunc = 0
        self.mesesdesem = 0

        self.mesesbenef = 0

    def calculo_beneficio(self):
        if (self.datanasc - date.year) >= 18:

            if self.categoria == 'Empregado':
                self.valorbase == 1000
                self.mesesbenef = 3
            elif self.categoria == 'desempregrado':
                self.mesesbenef = 6
                self.valorbase = 1500
                if self.mesesdesem < 6:
                    self.valorbase -= self.valorbase * 0.1
            elif self.categoria == 'empregador':
                self.valorbase == self.numerofunc * 200
                if self.numerofunc <= 50:
                    self.valorbase += self.valorbase/10

    def calculo_beneficios_especificos(self):
        if self.estado == 'PE':
            valor_por = self.valorbase * (14 / 100)
            self.valorfinal = self.valorbase + valor_por
