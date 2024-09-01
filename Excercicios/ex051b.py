"""
Desenvolva um programa que leia o ṕrimeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print("{:_^40}".format("PROGRESSÃO ARITMÉTICA"))
primeiro=int(input("Primeiro termo: "))
razao = int(input("Razao: "))
decimo = primeiro + (10 - 1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' ')
print('FIM')
