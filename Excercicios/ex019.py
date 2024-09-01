'''
Um professor quer sortear um de seus 4 alunos para apagar o quadro. Faça um programa que ajude ele.
Lendo o nome deles e escrevendo o escolhido.
'''
print('='*10, 'Sorteio', '='*10)

import random

nome1 = str(input('Primeiro nome: '))
nome2 = str(input('Segundo nome: '))
nome3 = str(input('Terceiro nome: '))
nome4 = str(input('Quarto nome: '))
lista = [nome1, nome2, nome3, nome4]
print('{} O seu nome foi o escolhido!'.format(random.choice(lista)))

