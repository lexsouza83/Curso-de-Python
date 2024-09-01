"""
Faça um programa que leia um número qualquer e mostre o seu Fatorial.
ex. 5! = 5x4x3x2x1 = 120
"""
from math import factorial
print("{:_^40}".format('CALCULANDO FATORIAL'))
n1 = int(input('Digite um número: '))
c = n1
fat = factorial(n1)
print('O fatorial de {}! = '.format(n1), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    c -= 1
print(fat)


