"""
Faça um programa que mostre a tabuada de vários números, um de cada vez para cada valor digitado pelo usuário.
O programa será interrompido quando o número socilitado for negativo.
"""
print('{:.^40}'.format('TABUADA 3.0'))
n1 = cont = t = 0
while True:
    n1 = int(input('Digite um número para mostrar sua tabuada: '))
    if n1 < 0:
        break
    for t in range(1, 11):
            t += 1
            print(f'{n1} x {t} = {t * n1:>}')
    print('-' * 30)
print('-'* 30)
print('PROGRAMA ENCENRADO')

