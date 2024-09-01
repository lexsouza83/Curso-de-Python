"""
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio.
Indo de 10 até 0, com uma pausa de 1 segundo eles.
"""
from time import sleep
import emoji
print('{:_^30}'.format('Cruzeiro Campeão!'))
for regressiva in range(10, -1, -1):
    print(regressiva)
    sleep(1)
print(emoji.emojize('\U0001f4a5  \U0001f4a5  \U0001f4a5'))



