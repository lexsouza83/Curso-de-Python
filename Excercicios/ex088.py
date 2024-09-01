"""
Faça um programa que ajude um jogador da e MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""
print('-'*40)
print('GERADOR DE PALPITES MEGA SENA')
print('-'*40)
from random import randrange
from time import sleep
palpites = []
j = 0
jog = int(input('Quantos jogos deseja criar? '))
print('Gerando palpite!')
sleep(1)
while j in range(0, jog):
    for p in range(0, 6):
        p1 = randrange(1, 60)
        palpites.append(p1)
        palpites.sort()
        sleep(1)
    print(f'{j + 1}º palpite: {palpites}')
    palpites.clear()
    j += 1
print('+'* 40)


