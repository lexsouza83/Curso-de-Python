"""
Crie um programa que leia vários números inteiros pelo teclado. O programa só  vai parar quando o usuário digitar o valor 999,
que é a condição de parada. No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
print('{:.^50}'.format('TRATANDO VALORES'))
n1 = 0
c = 0
soma = 0
n1 = int(input('Digite uma valor. [999 finaliza!]:  '))
while n1 != 999:
    c += 1
    soma = soma + n1
    n1 = int(input('Digite uma valor. [999 finaliza!]: '))
print('Vocẽ Digitou {} valores. A soma entre eles é: {}'.format(c, soma))
print('TERMINOU!')
