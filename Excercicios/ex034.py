'''
Escreva um programa que pergunte o salário de uma funcionario e calcule o aumento.
Para salários acima de R$1.250,00 calcule 10% de aumento.
Para os inferiores ou iguais, aumento de 15%
'''
print('______ AJUSTE DE SALÁRIO ______')
s = float(input('Qual é o seu salário? R$ '))
if s <= 1250:
    aj = (s * 15)/100
else:
    aj = (s * 10)/100

print('Quem recebia o salário de R${:.2f} passará a receber R${:.2f}'.format(s, (s + aj)))