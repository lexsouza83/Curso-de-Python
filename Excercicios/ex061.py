"""
Refaça o desafio 051, lendo o primeiro termo e a razão de PA, mostrando os 10 primeiros termos da prograssão
usando a estrutura While
"""
print("{:_^40}".format("PROGRESSÃO ARITMÉTICA"))
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
termo = primeiro
c = 1
while c <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    c += 1
print('FIM')
