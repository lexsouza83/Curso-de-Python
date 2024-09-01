'''
Escreva um programa  que leia a velocidade de um carrro.
Se el ultrapassar 80km/h, mostre a mensagem que ele foi multado.
A multa vai custar  R$7,00 por cada km acima do limite.
'''

print('______ RADAR ELETRÔNICO ______')
l = float(80)
v = int(input('Infore a velocidade do carro: '))
m = v - l
if v > 80:
    print('Você excedeu o limite de velocidade permitido! 80km/h'
          '\nMulta aplicada no valor de R${:.2f}'.format(float(m * 7)))
else:
    print('Velocidade dentro do limite'
          '\n TENHA UM ÓTIMO DIA, DIRIJA COM SEGURANÇA!')