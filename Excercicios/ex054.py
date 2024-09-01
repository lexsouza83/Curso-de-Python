"""
Crie um programa que leia o ano de nascimento de sete pessoas. No final mostre quantas pessoas ainda não atingiram
a maioridade e quantas já são maiores. OBS: Considere maioridade 21 anos
"""
from datetime import date
print('{:_^30}'.format(' CHECANDO MAIORIDADE '))
maior = 0
menor = 0
for i in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(i)))
    idade = (date.today().year - nasc)
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('-='* 20)
print('Temos {} maiores e {} menores de 21 anos.'.format(maior, menor))
print('-='* 20)
