"""
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário
quer ou não continuar.
No final mostre:
a) quantas pessoas tem mais de 18 anos;
b) quntos homens foram cadastrados;
c) quantas mulheres tem menos de 20 anos.


from time import sleep
print('{:.^40}'.format('CADASTRANDO PESSOAS'))
continuar = ''
c = 0
maisdeDezoito = 0
menosdeVinte = 0
totaldeHomens = 0

while continuar in 'S':
    idade = int(input('INFORME A IDADE: '))
    sexo = str(input('INFORME O SEXO [M/F]:'))
    continuar = str(input('DESEJA CONTINUAR? [S/N]: ')).strip().upper()
    c += 1
    print('{:.^40}'.format(''))
print('ANALISANDO...')
sleep(2)
if idade > 18:
    c = c
    maisdeDezoito = c

print(f'{maisdeDezoito} pessoas tem mais de 18 anos')
print('{:.^40}'.format(''))

"""
import re

nome = input("Digite o nome: ")

print(re.findall(r"[aeiou]", nome, re.IGNORECASE))
