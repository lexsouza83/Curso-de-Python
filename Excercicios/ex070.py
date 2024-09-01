"""
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
No final, mostre
a) Qual é o total gasto na compra;
b) Quantos produtos custam mais de R$1000;
c) Qual é o nome do produto mais barato.
"""
from time import sleep
print('EStatiscas em produtos')
c = totalCompra = total1000 = menorPreco = 0
barato = ''
while True:
    produto = str(input('Nome do Produto: ')).strip()
    preco = float(input('Preço do produto: '))
    c += 1
    totalCompra += preco
    if preco >= 1000:
        total1000 += 1
    if c == 1 or preco < menorPreco:
        menorPreco = preco
        barato = produto
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print('ANALISANDO DADOS')
sleep(2)
print(f'O total gasto nas compras foi: R${totalCompra} reais')
print(f'Temos {total1000} produto(s) custa(am) mais de R$ 1000.00 reais.')
print(f'{barato} é o produto com menor preço: R${menorPreco} reais')
print('FIM')