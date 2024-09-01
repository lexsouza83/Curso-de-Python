"""
Crie um programa onde o usuaário possa digitar sete valores numéricos e cadastre-os em uma única lista que mantenha
separados os valores pares e impares. No final mostre os valores pares e impares em ordem crescente.

Solução do professora Gustavo Guanabara

"""
num = [[], []] #Lista aninhada com 2 sublistas que vão separar os valores pares e impares.
valor = 0
#Laço for para separar o números pares e impares em suas devidsa sublisdtas.
for c in range(1, 8):
    valor = int(input(f'Digite o {c}º valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores impares digitados foram: {num[1]}')

