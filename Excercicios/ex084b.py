"""
Faça um programa que leia o nome e o peso de várias pessoas guardando-os dentro de uma lista. No final mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas mais pesadas;
c) Uma listagem com as pessoas mais leves.

Solução do desafio encontrada nos comentários da aula no Youtube
"""
pessoas = []
while True:
    nome = input('Nome da pessoa: ')
    peso = float(input('Informe o peso em KG: '))
    pessoas.append([nome,peso])
    continua = input('Quer continuar? [S/N] ')
    if continua in 'nN':
        break

peso_descrescente = sorted(pessoas, key=lambda p: p[1], reverse=True)
maior_peso, menor_peso = peso_descrescente[0][1], peso_descrescente[-1][1]
lista_maior_p = [pessoa[0] for pessoa in pessoas if pessoa[1] == maior_peso]
lista_menor_p = [pessoa[0] for pessoa in pessoas if pessoa[1] == menor_peso]
print('-='*25)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior_peso} kg. Peso de {lista_maior_p}')
print(f'O menor peso foi de {menor_peso} kg. Peso de {lista_menor_p}')