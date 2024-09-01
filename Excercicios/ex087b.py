"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado.
No final mostre a matriz na tela, com a formatação correta.

Solução do professor Gustavo Guanabara

"""
print('-'*35)
print('MATRIZ EM PYTHON')
print('-'*35)
matriz = [[0,0,0],[0,0,0],[0,0,0]]
spar = mai = scol= 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor para a posição [{l}, {c}]: '))
print('-'* 35)
for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]', end='')
        #Verificando os números pares
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
    print()
print('-'* 35)
print(f'A soma dos valores pares é: {spar}')
#Verificando os valores da 3ª coluna da matriz.
for l in range(0, 3):
    scol += matriz[l][2] #Aqui a posição da linha sempre se altera e da coluna é fixa.
print(f'A soma dos valores da 3ª coluna é: {scol}')
#Verificando o maior valor presente na segunda linha da matriz.
for c in range(0,3):
    if c == 0:
        mai = matriz[1][c] #Aqui a posição da linha é fixa e a da coluna sempre se altera.
    elif matriz[1][c] > mai:
        mai = matriz[1][c]

print(f'O maior valor da 2ª linha é: {mai}')
