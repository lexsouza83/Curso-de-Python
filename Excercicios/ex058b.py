"""
Melhore o desafio 028 onde o computaodr vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar
até acertar. Mostrando no final quantos palpites foram necessários para vencer.
"""
from random import randint
pc = randint(0, 10)
cont = 0
print("Sou o seu PC... Pensei em um número entre 0 e 10. Andivinhe qual foi!")
acertou = False
while not acertou:
    jogador = int(input('Qual a sua jogada? '))
    cont += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais...! Tente outra vez.')
        elif jogador > pc:
            print('Menos...! Tente outra vez.')
print('PARABÉNS! Você acertou na {}ª jogada.'.format(cont))

