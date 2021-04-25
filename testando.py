import datetime

def calculate_age(born):
    today = date.today()


def calculo():
    valor = int(input('Informe um valor'))
    porcentagem = int(input('Informe uma porcentagem'))

    valor_por = valor * (porcentagem/100)


    valor_final = valor + valor_por
    print(f'A porcentagem de {porcentagem}% é um valor de {valor_por}')
    print(f'O valor final é {valor_final}')

print(datetime.datetime.now())