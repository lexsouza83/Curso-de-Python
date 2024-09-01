"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.

"""
from time import sleep
print('-'*35)
print('MATRIZ EM PYTHON')
print('-'*35)
matriz = []
pos = 1
while pos in range(0, 10):
    matriz.append(int(input(f'Digite o {pos}º numero:  ')))
    pos += 1
print('-'*35)
print('Preechendo a Matriz...')
sleep(2)
#print(f'|{matriz[0:3]}|\n|{matriz[3:6]}|\n|{matriz[6:9]}|')
print('|{}|\n|{}|\n{}|'.format(matriz[0:3], matriz[3:6], matriz[6:9]))
print('-'*35)
print('Fim')