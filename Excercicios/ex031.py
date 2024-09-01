'''
Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando
R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
'''
print('______ CUSTO DA VIAGEM ______')
d = float(input('Qual é a distância da viagem: '))
if d <= 200:
    print('Com a distãncia de {}Km, o custo da viagem será RS{:.2f}.'.format(d, d * 0.50))
else:
    print('Com a distãncia de {}Km, o custo da viagem será RS{:.2f}.'.format(d, d * 0.45))
print('FAÇA UMA ÓTIMA VIAGEM!')