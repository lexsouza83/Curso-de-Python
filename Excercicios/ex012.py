'''
Faça um algoritmo que leia o preço de uma produto e mostre seu preço com 5% de desconto.
'''
preco = float(input('Infore o valor do produto: R$'))
desconto = (preco * 5) / 100
print('Com 5% de desconto, o valor pago será: R${:.2f}'.format(preco - desconto))

