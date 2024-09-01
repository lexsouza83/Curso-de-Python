"""
Melhore o desafio 028 onde o computaodr vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar. Mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
cont = 1
pc = randint(0, 10)
print('{:_^30}'.format('JOGO DA ADIVINHAÇÃO 2.0'))
print("""Adivinhe em que número eu pensei entre 0 e 10:
Tente descobrir qual foi.""")
jogador = int(input('Faça sua jogada: '))
while pc != jogador:
    jogador = int(input('ERRADO! Tente outra vez:  '))
    cont += 1
print('PARABÉNS! Você acertou na {}ª tentativa!'.format(cont))
