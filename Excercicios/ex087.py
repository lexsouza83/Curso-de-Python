"""
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma dos valores da terceira coluna;
c) O maior valor da segunda linha.

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
print('|{}|\n|{}|\n{}|'.format(matriz[0:3], matriz[3:6], matriz[6:9]))
print('-'*35)
print('Analisando os Valores')
sleep(2)
somap = 0
for p in matriz:
    if p % 2 == 0:
        somap = somap + p
print(f'A soma dos números pares é: {somap}')
somac = matriz[2] + matriz[5] + matriz[8]
print(f'A soma dos valores da 3ª coluna é: {somac}')
maior = max(matriz[3], matriz[4], matriz[5])
print(f'O maior valor da 2ª linha é: {maior}')
print('-'*35)

print(f'Fim')