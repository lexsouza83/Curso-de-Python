'''
Refaça o DESAFIO 035 dos Triângulos acrescentando o recurso de mostra que tipo de triângulo será formado.
 - Equilátero : todos os lados igual.
 - Isósceles: dois lados iguais.
 - Escaleno: todos os lados diferentes.
'''

print('______ ANALISANDO TRIÂNGILO ______')
r1 = float(input('Informe o comprimento da reta 1: '))
r2 = float(input('Informe o comprimento da reta 2: '))
r3 = float(input('Informe o comprimento da reta 3: '))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print('As retas 1, 2 e 3 formam um Triângulo.')
    if r1 == r2 and r2 == r3:
        print('O Triângulo formado é Equilátero!')
    elif r1 != r2 and r2 != r3 and r1 != r3:
        print('O Triângulo foramdo é Escaleno')
    else:
        print('O Triângulo formado é Isósceles')
else:
    print('As retas 1, 2 e 3 não formam um Triângulo.')
