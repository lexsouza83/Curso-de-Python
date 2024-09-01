"""
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso mostre a listagem de números gerados e também indique o menor e o maior número que está na tupla
"""
from random import sample
a = tuple(sample(range(10), 5))
print(f'Valores sorteados: {a}')
print(f'O maior valor é: {max(a)}\nO menor valor é: {min(a)}')