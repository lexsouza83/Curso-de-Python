"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas que vão conter apenas os valores pares e os valores impares digitados respectivamente.
Ao final, mostre o contéudo das três listas geradas.
"""
from time import sleep
print('-='* 15)
print('Criando Várias Listas')
print('-='* 15)
listaG = []
listaP = []
listaI = []
n1 = 0
pos = 0
while True:
    n1 = int(input(f'Digite o {pos + 1}º número: '))
    listaG.append(n1)
    if n1 % 2 == 0:
        listaP.append(n1)
    else:
        listaI.append(n1)
    pos += 1
    op = ' '
    while op not in 'SN':
        op = str(input('Continuar? S/N ')).upper().strip()
    if op == 'N':
        break
print('-='* 15)
print('ANALISANDO NÚMEROS INFORMADOS')
print('-='* 15)
sleep(3)
print(f'Lista geral: {listaG}')
print(f'Lista de números pares: {listaP}')
print(f'Lista de números impares: {listaI}')
