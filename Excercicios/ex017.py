'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e
mostre o comprimento da sua hipotenusa.
'''
print('=' * 20, 'Calculando Hipotenusa', '=' * 20)

from math import hypot

cop = float(input('Inforeme o comprimento do cateto oposto: '))
cad = float(input('Informe o comprimento do cateto adjacente: '))
print('O comprimento da Hipotenusa é: {:.2f}'.format(hypot(cop, cad)))
