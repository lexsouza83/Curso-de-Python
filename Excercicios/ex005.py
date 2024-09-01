'''
Faça uma programa que leia um número inteiro e mostre  na tela o seu sucessor e o seu antecessor.
'''
print('='*10, 'Antecessor e Sucessor','='*10)

n1 = int(input('Informe um número: '))
print('O número informado é o {}, seu Antecessor é {} e o Sucessor é {}.'.format(n1, n1-1, n1+1))
