'''
Crie um programa que faça o computador jogar Jokenpô com você.

'''

from random import randint
from time import sleep
print('{:_^30}'.format(' VAMOS JOGAR JOKENPÔ '))
escolhapc = (randint(1, 4))
opcao = ('','PEDRA','PAPEL','TESOURA', '')
pc = opcao[escolhapc]
escolhajog = int(input('''Faça sua escolha: 
    [1] PEDRA
    [2] PAPEL
    [3] TESOURA
    Sua escolha:  '''))
jogador = opcao[escolhajog]
print('JO')
sleep(1)
print('     KEN')
sleep(1)
print('             PÔ')
print('O pc jogou {} e você jogou {}'.format(pc, jogador))

if pc == jogador:
    print('EMPATE, tente outra vez!')
elif pc == 'PAPEL'and jogador == 'PEDRA':
    print('O papel embrulha a pedra. PC VENCEU!')
elif pc == 'PEDRA' and jogador == 'TESOURA':
    print('A Pedra quebra a Tesoura. PC VENCEU!')
elif pc == 'TESOURA' and jogador ==  'PAPEL':
    print('A Tesoura corta o papel. PC VENCEU!')
elif pc == 'PEDRA' and jogador == 'PAPEL':
    print('O papel embrulha a pedra. VOCÊ VENCEU!')
elif pc == 'TESOURA' and jogador == 'PEDRA':
    print('A Pedra quebra a Tesoura. VOCÊ VENCEU!')
elif pc =='PAPEL' and jogador == 'TESOURA':
    print('A Tesoura corta o papel. VOCẼ VENCEU!')
elif jogador != 'PEDRA' and 'PAPEL' and 'TESOURA':
    print('Opção inválida! tente outra jogada!')
