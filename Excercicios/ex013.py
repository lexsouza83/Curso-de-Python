'''
Faça um algoritmo que leia o salário de um funcionário e mostra o seu novo salário com 15% de aumento.
'''
print('='*15,'Aumento Salarial','='*15)
salario = float(input('Infore o valor do salário: R$'))
aumento = (salario * 15) / 100
print('Com 15% de acrescimo, o salário chega ao valor de: R${:.2f}'.format(salario + aumento))
