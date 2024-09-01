"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
a) Quantos números foram digitados;
b) A lista de números, ordenanda de forma decrescente;
c) Se o valor 5 foi digitado e está ou não na lista.
"""
print('-='*30)
print('OPERAÇÃO COM LISTAS')
print('-='*30)
lista = []
pos = 0
n1 = 0
while True:
    n1 = int(input(f'Informe o {pos+1}º número: '))
    lista.append(n1)
    lista.sort()
    lista.reverse()
    pos += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Deseha continuar? S/N: ')).strip().upper()
    if resp == 'N':
       break

print('-='*30)
print('ANALISANDO OS DADOS INFORMADOS')
print(f'Ao todo foram informados {len(lista)} números')
print('-='*30)
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 não esta na lista!')
print('-='*30)
print(f'Lista em ordem decrescente: {lista}')