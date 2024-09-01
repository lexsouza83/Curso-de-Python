'''
Crie uma programa que leia quanto dinheiro uma pessa tem na carteira e mostre quantos Dólares ela pode comprar
Considere o valor do Dóllar = R$3.27
'''
print('='*15, 'CASA DE CAMBIO', '='*15)
real = float(input('Informe o valor em dinheiro: R$'))
dolar = float(input('Infore a cotação do dia: '))
print('Com o valor de: R${} é possivel comprar US${:.2f} dolares.'.format(real, real / dolar))