"""
Desenvolva um programa que leia o ṕrimeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print("{:_^40}".format("PROGRESSÃO ARITMÉTICA"))
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
n = int(input("Quantos termos deseja exibir: "))

ultimo = primeiro + (n-1)*razao
ultimo = ultimo + 1

for var in range(primeiro, ultimo, razao):
    print(var, end=' ')
print('FIM')