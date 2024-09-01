"""
Crie um programa que simule o funcionamento de um Caixa Eletrônico. No início pergunte ao usuário qual será o valor a ser sacado (num int)
 e o programa vai informar quantas cédulas de cada valor seráo entregues.
Obs: Conseidere que o caixa possui cédulas de 1, 10, 20 e 50 reais.
"""
#CORREÇÃO DO GUANABARA
from time import sleep
print(':'* 50)
print('{:^50}'.format('POTÉBANK'))
print(':'* 50)
valor = int(input('Qual o valor que deseja sacar: R$ '))
total = valor
ced = 200
totalced = 0
print(':'* 50)
print('{:^50}'.format('AGUARDE CONTANDO CÉDULAS'))
print(':'* 50)
sleep(3)
while True:
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Total de {totalced} cédulas de R${ced}')
        if ced == 200:
            ced = 100
        if ced == 100:
            ced = 50
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break

print(':'* 50)
print('{:^50}'.format('POR FAVOR CONFIRA SEU DINHEIRO!'))
print(':'* 50)
sleep(3)
print('{:^50}'.format('Obrigado por usar o POTÉBANK. Tenha um bom dia!'))
