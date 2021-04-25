from pessoa import Pessoa, contar_numero_beneficiados as contar, beneficiarios_por_valor, valor_total_beneficio
from datetime import date

lista_pessoa = []
fim = False
while not fim:
    pessoa = Pessoa()
    print('Bem Vindo')
    pessoa.nome = input('Informe seu nome completo')
    pessoa.datanasc = int(input('Informe o ano em que você nasceu'))
    pessoa.estado = input('Informe a sigla do seu estado')
    pessoa.categoria = input('Informe se você está empregado, desempregado, ou é um empregrador')
    if pessoa.categoria == 'Empregado':
        ok = False
        while not ok:
            resp = input('Você é aposentado? Responda com s/n')
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
    print('='*50)
    print('O nome informado foi {}'.format(pessoa.nome))
    print('A data de nascimento é {}'.format(pessoa.datanasc))
    print('A categoria dessa pessoa é {}'.format(pessoa.categoria))
    print('Essa pessoa atendeu as seguintes regras')
    for i in pessoa.regras:
        print(i)
    print('Portanto, recebera R${}'.format(pessoa.valorfinal))
    print('durante {} meses'.format(pessoa.mesesbenef))
    resp = False
    while not resp:
        op = input('Deseja cadastrar uma nova pessoa? s/n')
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
print('No total foram cadastrados {} usuarios'.format(len(lista_pessoa)))
print('do qual {} pessoas se qualificaram para receber o beneficio'.format(contar(lista_pessoa)))
print('Ao todo, será pago R${} entre todos os beneficiarios'.format(valor_total_beneficio(lista_pessoa)))
print('As duas pessoa com o maior valor são {}, que vai receber R${}'.format(beneficiarios_valor[0].nome, beneficiarios_valor[0].valorfinal))
print('E {}, que vai receber R${}'.format(beneficiarios_valor[1].nome, beneficiarios_valor[1].valorfinal))