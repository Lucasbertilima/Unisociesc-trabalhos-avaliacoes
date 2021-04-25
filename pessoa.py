import datetime
from typing import List

regras = {'L': 'L - O benefício será de 6 meses para desempregados', 'U': 'U - O Benefício será de 3 meses para empregados',
          'C': 'C - Para empregadores que tenham até 50 funcionários haverá um acréscimo de 10% sobre o valor total',
          'A': 'A - O benefício só será concedido para maiores de 18 anos', 'S': 'S - O benefício de pessoas que moram em Pernambuco terá acréscimo de 14%',
          'H': 'H - Se estiver desempregado há menos de 6 meses terá uma redução de 10%'}


class Pessoa:
    def __init__(self):
        self.nome = ''
        self.datanasc = ''
        self.categoria = ''
        self.estado = ''
        self.aposentado = False
        self.valorinicial = 0
        self.valorfinal = 0
        self.numerofunc = 0
        self.mesesdesem = 0
        self.regras = []
        self.mesesbenef = 0

    def verificar_maior_idade(self):
        agora = datetime.datetime.now()
        if (int(agora.year) - self.datanasc) >= 18:
            self.regras.append(regras['A'])
            return True
        else:
            return False

    def calculo_tempo_beneficio(self):
        if self.categoria == 'Empregado':
            self.mesesbenef = 3
            self.valorfinal = self.valorinicial
            self.regras.append(regras['U'])
        elif self.categoria == 'Desempregado':
            valor = 0
            if self.mesesdesem < 6:
                valor = self.valorinicial / 10
                self.valorfinal = self.valorinicial - valor
                self.regras.append(regras['H'])
            else:
                self.valorfinal = self.valorinicial
            self.mesesbenef = 6
            self.regras.append(regras['L'])
        else:
            self.mesesbenef = 2

    def calculo_beneficio(self):
        valor = 0
        if self.verificar_maior_idade():
            if self.categoria == 'Empregado':
                self.valorinicial = 1000
            elif self.categoria == 'Desempregado':
                self.valorinicial = 1500
            elif self.categoria == 'Empregador':
                self.valorinicial = self.numerofunc * 200
                if self.numerofunc <= 50:
                    valor = self.valorinicial/10
                    self.valorfinal = self.valorinicial + valor
                    self.regras.append(regras['C'])
                    return valor
                self.valorfinal = self.valorinicial

    def calculo_beneficios_especificos(self):
        valor = 0
        if self.estado == 'PE':
            valor_por = self.valorfinal * (14 / 100)
            self.valorfinal = self.valorfinal + valor_por
            self.regras.append(regras['S'])
            return valor
        else:
            pass


def contar_numero_beneficiados(lista_cadastro: List[Pessoa]):
    numero_beneficiados = 0
    for i in lista_cadastro:
        agora = datetime.datetime.now()
        if (agora.year - i.datanasc) > 18:
            numero_beneficiados += 1
    return numero_beneficiados


def valor_total_beneficio(lista_cadastro: List[Pessoa]):
    valor_beneficio = 0
    for i in lista_cadastro:
        agora = datetime.datetime.now()
        if (agora.year - i.datanasc) > 18:
            valor_beneficio += i.valorfinal
    return valor_beneficio


def beneficiarios_por_valor(lista_cadastro: List[Pessoa]):
    maiores = []
    lista_beneficiarios = []
    for i in lista_cadastro:
        if i.verificar_maior_idade():
            lista_beneficiarios.append(i)
    lista_valores = []
    for i in lista_beneficiarios:
        lista_valores.append(i.valorfinal)
    lista_valores.sort(reverse=True)
    for i in lista_valores:
        for j in lista_beneficiarios:
            if i == j.valorfinal:
                maiores.append(j)

    return maiores


def beneficiarios_por_tempo(lista_cadastro: List[Pessoa]):
    maiores = []
    lista_beneficiarios = []
    for i in lista_cadastro:
        if i.verificar_maior_idade():
            lista_beneficiarios.append(i)
    lista_tempos = []
    for i in lista_beneficiarios:
        lista_tempos.append(i.mesesbenef)
    lista_tempos.sort(reverse=True)
    for i in lista_tempos:
        for j in lista_beneficiarios:
            if i == j.mesesbenef:
                maiores.append(j)

    return maiores