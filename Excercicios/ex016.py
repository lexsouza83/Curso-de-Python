'''
Crie um programa que leia um número Real qualquer pelo teclado e mostre an tela a sua porção inteira.
'''

from math import trunc
n1 = float(input('Informe um número qualquer: '))
print('A parte inteira de {} é igual a {}'.format(n1, trunc(n1)))
