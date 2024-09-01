"""
Faça um program que jogue PAR ou IMPAR com o computador. O jogo será interrompido quando o jogador PERDER mostrando
o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
from time import sleep
from random import randint
print('{:.^40}'.format('JOGANDO PAR OU IMPAR'))
p = jog = c = s = 0

while True:
    jog = int(input('Digite um número: '))
    pc = randint(0, 10)
    s = pc + jog
    op = ' '
    while op not in 'PI':
        op = str(input('Escolha PAR  ou IMPAR. [P/I] ')).strip().upper()[0]
    print(f'Você jogou {jog} e o PC jogou {pc}. Total {s} ', end='')
    print('DEU PAR ' if s % 2 == 0 else 'DEU IMPAR')
    if op == 'P':
        if s % 2 == 0:
            print('VOCẼ GANHOU!')
            c += 1
        else:
            print('VOCÊ PERDEU!')
            break
    elif op == 'I':
        if s % 2 == 1:
            print('VOCẼ GANHOU!')
            c += 1
        else:
            print('VOCÊ PERDEU!')
            break
    print('jogue novamente...')
print(f'Vocẽ Ganhou {c} vezes.')
print('JOGO ENCERRADO')

