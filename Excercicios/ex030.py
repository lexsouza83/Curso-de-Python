'''
Crie um program que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.
'''
print('______ PAR ou IMPAR ______')
n1 = int(input('Digite um número qualquer: '))
if n1 % 2 == 0:
    print('O número {} é par'.format(n1))
else:
    print('O número {} é impar'.format(n1))