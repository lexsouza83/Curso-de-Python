'''
Elabora um programa que calcule o valor a ser pago por um produto, considerando o seu Preço Normal e
Condições de pagamento:

- À vista dinheiro / cheque: 10% de desconto.
- À vista no cartão 5% de desconto
- Em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros.
'''
print('______ FORMAS DE PAGAMENTO ______')
preco = float(input('Informe o valor do Produto R$ '))
opcao = int(input('''Escolha a forma de pagamento:
    [1] À VISTA DINHEIRO/CHEQUE.
    [2] À VISTA NO CARTÃO.
    [3] 2x NO CARTÃO.
    [4] 3x OU MAIS NO CARTÃO. '''))
print('Sua opção: {}'.format(opcao))
if opcao == 1:
    total = preco - (preco * 10 / 100)
elif opcao == 2:
    total = preco - (preco * 5 / 100)
elif opcao == 3:
    total = preco
    parcelas = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS!'.format(parcelas))
elif opcao == 4:
    total = preco + (preco * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcelas = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS!'.format(totalparc, parcelas))
else:
    total = preco
    print('Opção Invalida! Escolha novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} ao ser concluida.'.format(preco, total))
