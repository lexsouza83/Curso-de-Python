'''
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.
'''
print('=' * 10, 'Calculando Hipotenusa', '=' * 10)

from math import sin, cos, tan, radians

ang = float(input('Informe o valor do ângulo: '))
print('Analisando o ângulo informado'
      '\nO seu seno é igual a {:.2f}'
      '\nO seu cosseno é igual a {:.2f}'
      '\nSua tangente é igual a {:.2f}'.format(sin(radians(ang)), cos(radians(ang)), tan(radians(ang))))
