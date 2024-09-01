"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado em suas respectivas posições na lista.
"""
from time import sleep

print('.'* 40)
print('{:^40}'.format('ANALISANDO NÚMEROS'))
print('.'* 40)
num = list()
for cont in range(0, 5):
    num.append(int(input(f'Digite um número para a {cont}ª posição: ')))
print('.'* 40)
print('{:^40}'.format('...ANALISANDO...'))
print('.'* 40)
sleep(2)
print(f'Os números informados foram: {num}')
print(f'O maior número infomado foi: {max(num)}, na(s) posição(ções): ', end='')
for c, p in enumerate(num):
    if p == max(num):
        print(f'{c}...', end='')

print(f'\nO menor número informado foi : {min(num)}, na(s) posição(ções): ', end='')
for c, p in enumerate(num):
    if p == min(num):
        print(f'{c}...', end='')

