'''
Escreva um programa para aprovar um emprestimo bancario para a compra de uma casa.
O prograama vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o emprestimo
será negaado.
'''

comprador = str(input('Informe o seu nome: '))
valorimovel = float(input('Informe o valor do Imovel: R$ '))
salario = float(input('Qual o valor do seu salário: R$ '))
paganos = float(input('Em quantos anos de financiamento? '))
minimo = salario * 30 / 100
prestacao = valorimovel / (paganos * 12)
if prestacao >= minimo:
    print('!!!SOLICITAÇÃO NEGADA!!!'
          '\nInfelizmente senhor(a) {} o seu pedido de emprestimo foi negado!'
          '\nO valor da prestação supera 30% do salário do comprador!'.format(comprador))
else:
    print('!!!SOLITICAÇÃO APROVADA!!!'
          '\nParabéns Senhor(a) {} o seu pedido foi aprovado.'
          '\nTenha um ótimo dia!'.format(comprador))
