from pessoa import Pessoa, contar_numero_beneficiados as contar, beneficiarios_por_valor, valor_total_beneficio, beneficiarios_por_tempo
from datetime import date

lista_pessoa = []
fim = False
while not fim:
    pessoa = Pessoa()
    print('Bem Vindo')
    pessoa.nome = input('Informe seu nome completo')
    pessoa.datanasc = int(input('Informe o ano em que você nasceu'))
    pessoa.estado = input('Informe a sigla do seu estado').upper()
    while True:
        op = input('Você é \n1 - Empregado \n2 - Desempregado \n3 - Empregador')
        if op == '1':
            pessoa.categoria = 'Empregado'
            break
        elif op == '2':
            pessoa.categoria = 'Desempregado'
            break
        elif op == '3':
            pessoa.categoria = 'Empregador'
            break
        else:
            print('Categoria invalida, tente novamente')


    if pessoa.categoria == 'Empregado':
        ok = False
        while not ok:
            resp = input('Você é aposentado? Responda com s/n').lower()
            if resp == 's':
                pessoa.aposentado = True
                ok = True
            elif resp == 'n':
                pessoa.aposentado = False
                ok = True
            else:
                resp = input('Opção invalida. Tente novamente')

    elif pessoa.categoria == 'Desempregado':
        ok = False
        while not ok:
            pessoa.mesesdesem = int(input('Informe a quantos meses está desempregado'))
            ok = True
            break
    elif pessoa.categoria == 'Empregador':
        ok = False
        while not ok:
            qtdfunc = int(input('Informe a quantidade de funcionários que sua empresa tem'))

            pessoa.numerofunc = qtdfunc
            ok = True
            break
    pessoa.calculo_beneficio()
    pessoa.calculo_tempo_beneficio()
    pessoa.calculo_beneficios_especificos()
    lista_pessoa.append(pessoa)
    print('='*100)
    print('O nome informado foi {}'.format(pessoa.nome))
    print('A data de nascimento é {}'.format(pessoa.datanasc))
    print('A categoria dessa pessoa é {}'.format(pessoa.categoria))
    print('Essa pessoa atendeu as seguintes regras')
    print('='*100)
    for i in pessoa.regras:
        print(i)
    print('Portanto, recebera R${}'.format(pessoa.valorfinal))
    print('durante {} meses'.format(pessoa.mesesbenef))
    print('='*100)
    resp = False
    while not resp:
        op = input('Deseja cadastrar uma nova pessoa? s/n').lower()
        if op == 's':
            resp = True
            fim = False
        elif op == 'n':
            fim = True
            break
        else:
            print('Opção invalida')
            resp = False

beneficiarios_valor = beneficiarios_por_valor(lista_pessoa)
beneficiarios_tempo = beneficiarios_por_tempo(lista_pessoa)
print('='*100)
print('No total foram cadastrados {} usuarios\n'.format(len(lista_pessoa)))
print('do qual {} pessoas se qualificaram para receber o beneficio\n'.format(contar(lista_pessoa)))
print('Ao todo, será pago R${} entre todos os beneficiarios\n'.format(valor_total_beneficio(lista_pessoa)))
print('Quem vai receber o maior valor é {}, que vai receber R${}\n'.format(beneficiarios_valor[0].nome, beneficiarios_valor[0].valorfinal))
if len(beneficiarios_valor) > 2:
    print('E {}, que vai receber R${}\n'.format(beneficiarios_valor[1].nome, beneficiarios_valor[1].valorfinal))
print('E quem vai receber o beneficio por mais tempo é {}\n'.format(beneficiarios_tempo[0].nome))
print('Que vai receber o beneficio por {} meses\n'.format(beneficiarios_tempo[0].mesesbenef))
if len(beneficiarios_tempo) > 2:
    print('E {}, que vai receber por {} meses'.format(beneficiarios_tempo[1].nome, beneficiarios_tempo[1].mesesbenef))