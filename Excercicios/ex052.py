"""
Faça un programa que leia um número inteiro e diga se ele é ou não um número primo.
"""
print("{:_^30}".format("NÚMEROS PRIMOS"))
total = 0
num = int(input("Digite um número: "))
for cont in range(1, num+ 1):
    if num % cont == 0:
        print('\033[33m', end=' ')
        total += 1
    else:
        print('\033[31m', end=' ')
    print('{}'.format(cont), end=' ')
print("\n\033[mO número {} é divisível por {} números.".format(num, total))

if total == 2:
    print('Elé é primo.')
else:
    print('Ele não é primo.')
