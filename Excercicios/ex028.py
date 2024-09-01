'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuario tentar
descobrir qual o foi o número escolhido pelo computador.
o pc deverá escrever na tela se o o usuário venceu ou perdeu.
'''
from random import randint
from time import sleep
print('______ JOGO DA ADIVINHAÇÃO ______')
n1 = randint(0, 5)
resp = int(input('Adivinhe em que número eu pensei entre 0 e 5: '))
print('PROCESSANDO...')
sleep(3)
if resp == n1:
    print('Você acertou, PARABÉNS!')
else:
    print('Não foi dessa vez. Tente outra vez!')
