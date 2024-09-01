"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999.
Que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles.
Desconsiderando a flag.
"""
print('{:.^40}'.format('ANALISANDO NÚMEROS'))
n1 = c = soma = 0
while True:
    n1 = int(input('Digite um número para análise ou 999 para SAIR: '))
    if n1 == 999:
        break
    c += 1
    soma += n1
print(':'* 60)
print(f'{c} números foram digitados'
      f' e a Soma entre eles é igual a {soma}')
print(':'* 60)
print('ANÁLISE ENCERRADA!')
