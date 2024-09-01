"""
Faça um programa que leia o nome e o peso de várias pessoas guardando-os dentro de uma lista. No final mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves.

Solução do professor Gustavo Guanabara
"""

temp = [] # lista temporária
princ = []
mai = men = 0 #variáveis para os menores e maiores pesos.
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1] #temp na posição 1 indica o peso digitado
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:]) # [:] gera uma cópia da lista desejada.
    temp.clear() #limpa o conteúdo da lista indicada.
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break

print('-='* 30)
print(f'Ao todo, você cadasttrou {len(princ)} pessoas.')
print(f'O maior peso foi de {mai}KG. Peso de ', end='')
#Laço para encontrar o nome da pessoa que tem o maior peso.
for p in princ:
    if p[1] == mai:
        print(f'[{p[0]}]')
print(f'O menor peso foi de {men}KG. Peso de ', end='')
#Laço para encontrar o nome da pessoa que tem o menor peso.
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end='')