"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final mostre:
a) Quantas vezes apareceu o valor 9;
b) em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.

"""
print('.'* 30)
print('{:^30}'.format('ANALISANDO NÚMEROS'))
print('.'* 30)
valores = 0
valores = tuple(int(input(f'Digite o {c}° número: '))for c in range(1,5))
print(f'Os valores digitado foram: {valores}')
print(f'O número 9 apareceu {valores.count(9)} vezes')
if 3 in valores:
    print(f'O número 3 apareceu na {valores.index(3)+1}ª posição')
else:
    print('O número 3 não foi informado!')
print(f'Os números pares informados são: ', end='')
for n in valores:
    if n % 2 == 0:
        print(n, end=',')


