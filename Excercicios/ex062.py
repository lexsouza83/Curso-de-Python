"""
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerra quando ele disser que quer mostrar 0 termos.
"""
print("{:_^40}".format("PROGRESSÃO ARITMÉTICA"))
primeiro = int(input("Primeiro termo: "))
razao = int(input("Razao: "))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos deseja mostrar a mais: '))
print('FIM')
