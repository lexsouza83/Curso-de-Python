"""
Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 a 50.
"""
print('{:_^30}'.format('CONTAGEM DE PARES'))
print('Entre 1 e 50, São números Pares:')
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=' ')
print('FIM!')


