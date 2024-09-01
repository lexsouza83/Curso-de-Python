'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
ex: Digite um número: 11834
unidade: 4
dezena: 3
centena 8
milhar 1
'''

print('='*20, 'ANALIANDO NÚMEROS', '='*20)
n1 = int(input('Por favor informe um número: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10
print('Decompondo o número digitado')
print('Unidade: {}'
      '\nDezena: {}'
      '\nCentena: {}'
      '\nMilhar: {}'.format(u,d,c,m))
