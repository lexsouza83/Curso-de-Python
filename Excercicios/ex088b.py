"""
Faça um programa que ajude um jogador da e MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta
"""
print('-'*40)
print('GERADOR DE PALPITES MEGA SENA')
print('-'*40)
from random import randrange, sample
from time import sleep
palpites = []
j = 0
jog = int(input('Quantos jogos deseja criar? '))
print('+ '* 5,'Gerando palpites!','+ '* 5)
sleep(1)
while j in range(0, jog):
    palpites.append(sample(range(1, 61),6))
    palpites.sort()
    sleep(1)
    print(f'{j + 1}º palpite: {palpites}')
    palpites.clear()
    j += 1
print('+ '* 5, 'Boa Sorte!', '+ '* 5)


