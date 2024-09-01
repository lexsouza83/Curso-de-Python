'''
Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuario se elas podem ou não formar
um triângulo.
'''
print('______ ANALISANDO TRIÂNGILO ______')
r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas 1, 2 e 3 formam um Triângulo.')
else:
    print('As retas 1, 2 e 3 não formam um Triângulo.')
