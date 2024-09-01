"""
Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual
foi o maior e o menor valores lidos.O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
from time import sleep
print('{:.^40}'.format('ANALISANDO NÚMEROS'))
p = ''
cont = soma = num = media = n1 = maior = menor = 0
while p in 'Ss':
    num = int(input('Digite um número: '))
    p = str(input('Quer digitar outro número? SIM/NÃO '))[0]
    cont += 1
    soma += num
    media = soma / cont
    if cont == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        elif num < menor:
            menor = num
print(':'*40)
print('ANALISANDO...')
sleep(2)
print(':'*40)
print("""- {} números foram digitados
- A Soma entre ele é igual a {}
- A média entre eles é {} 
- O maior número digitado foi {}
- O menor número digitado foi {} """.format(cont, soma, media, maior, menor))
print('FIM DA ANÁLISE')

