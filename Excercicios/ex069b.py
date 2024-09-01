"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar.
No final mostre:
a) quantas pessoas tem mais de 18 anos;
b) quntos homens foram cadastrados;
c) quantas mulheres tem menos de 20 anos.

"""
# CORREÇÃO DO GUANABARA
from time import sleep
total18 = totalHomens = totalMulheres20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F]')).strip().upper()[0]

    if idade >= 18:
        total18 += 1
    if sexo == 'M':
        totalHomens += 1
    if sexo == 'F' and idade < 20:
        totalMulheres20 += 1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('{:.^40}'.format(''))
print('ANALISANDO INFORMAÇÕES...')
sleep(2)
print('{:.^40}'.format(''))
print(f'{total18} pessoas com mais de 18 anos.')
print('{:.^40}'.format(''))
print(f'{totalHomens} homen(s) foram cadastrados.')
print('{:.^40}'.format(''))
print(f'{totalMulheres20} mulheres com menos de 20 anos.')

