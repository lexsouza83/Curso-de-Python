"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.

Solução do professor Gustavo Guanabara

"""
print('-'*35)
print('MATRIZ EM PYTHON')
print('-'*35)
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para a posição [{l}, {c}]: '))
print('-'* 35)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
    print()