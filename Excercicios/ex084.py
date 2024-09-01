"""
Faça um programa que leia o nome e o peso de várias pessoas guardando-os dentro de uma lista. No final mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves.

"""

print('-='* 20)
print('PESANDO AS PESSOAS')
print('-='* 20)

pessoas = []
while True:
    nome = str(input('Digite seu nome: ')).capitalize().strip()
    peso = float(input('Digite seu peso (KG): '))
    pessoas.append([nome, peso])
    continuar = str(input('Informar mais dados? [S/N]: ')).upper().strip()[0]
    if continuar in 'nN':
        break
# Varivavel para ordenação da lista pessoas de forma reversa
peso_descrescente = sorted(pessoas, key=lambda p: p[1], reverse=True)

print('-='* 20)
print('ANALISANDO DADOS')
print('-='* 20)

print(f'Ao todo {len(pessoas)} pessoas foram cadastradas.')
print(pessoas, 'lista geral')

