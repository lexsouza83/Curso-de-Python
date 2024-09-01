"""
Crie um programa onde o usuário possa digitar vários valores numéricos e codastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado. No final seráo exibidos todos os valores únicos digitados,
em ordem crescente.
"""
print('.' * 40)
print('{:^40}'.format('CADASTRANDO VALORES'))
print('.' * 40)
listaValores = []
valores = 0
while True:
    valores = int(input('Informe uma valor: '))
    if valores not in listaValores:
        listaValores.append(valores)
        print('Número Salvo!')
    else:
        print('Este número já existe!')
    op = ' '
    while op not in 'SN':
        op = str(input('Quer informar outro? S/N: ')).strip().upper()
    if op == 'N':
        break
print('.' * 40)
print(sorted(listaValores))



