'''
A confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre
sua categoria com a idade.

- Até 9 anos : Mirin
- Até 14 anos : Infantil
- Até 19 anos : junior
- Até 25 anos Seniors
- Acima; Master
'''
print('_____ CATEGORIAS DOS ATLETAS _____')
from datetime import date
nasc= int(input('Digite o seu ano de Nascimento: '))
anoatual = date.today().year
idade = anoatual - nasc
print('Este(a) atleta em {} tem {} anos.'.format(anoatual, idade))
if idade <= 9:
    print('Classificação:  MIRIN.')
elif idade <= 14:
    print('Classificação: INFANTIL.')
elif idade <= 19:
    print('Classificação: JUNIOR.')
elif idade <= 25:
    print('Classificação: SÊNIOR.')
else:
    print('Classificação: MASTER')
