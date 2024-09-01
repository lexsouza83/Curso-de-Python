"""
Crie um programa onde o usuaário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha
separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.

"""
print('-'*35)
print('LISTANDO NÚMEROS PARES E IMPARES')
print('-'*35)
num = []
pos = 1
while pos in range(0, 8):
    n1 = int(input(f'Digite o {pos}º número: '))
    num.append(n1)
    pos += 1
print('-'* 35)
#print(f'lista geral: {sorted(num),}',)
print('-'* 35)
print(f'Números pares informados: ',end='')
for p in num:
    if p % 2 == 0:
        print(f'{p} ',end='')
print()
print(f'Números impares informados:', end='')
for i in num:
    if i % 2 != 0:
        print(f'{i} ')

print('Fim')