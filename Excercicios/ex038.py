'''
Escreva um programa que leia dois números inteiros e compare-os, mostrando  na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- Não existe número maior, os dois são iguais.
'''
print('_____ANALISANDO NÚMEROS_____')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
if n1 > n2:
    print('O primeiro valor é MAIOR!')
elif n1 < n2:
    print('O segundo valor é MAIOR!')
else:
    print('Não existe valor maior, os dois são IGUAIS!')
