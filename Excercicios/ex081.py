"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de números, ordenanda de forma decrescente;
c) Se o valor 5 foi digitado e está ou não na lista.
"""
print('-='*40)
print('OPERAÇÃO COM LISTAS')
print('-='*40)
lista = []
pos = 0
n1 = 0
ind = int(input('Informe quantos números pretende digitar:  '))
while pos < ind:
    n1 = int(input(f'Digite o {pos + 1}º número: '))
    lista.append(n1)
    pos += 1
print('-='*40)
print('ANALISANDO OS DADOS INFORMADOS')
print(f'Ao todo foram informados {ind} números')
print('-='*40)
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não esta na lista!')
print('-='*40)
lista.sort()
lista.reverse()
print(f'lista em order decrescente: {lista}')