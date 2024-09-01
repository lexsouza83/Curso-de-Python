"""
Desenvolva um programa que leia o nome, idade, e o sexo de 4 pessoas.
No final do programa, mostre:
- A média de idade do grupo:
- Qual é o homem mais velho:
- Quantas mulheres tem menos de 20 anos.
"""
print('{:_^30}'.format(' ANALISADOR COMPLETO '))
#obtendo dados.
somaidade = 0
mediaidade = 0
maioridadeh = 0
nomehvelho = ''
totalmulher20 = 0
for p in range(1, 5):
    nome = str(input("Qual é o seu Nome: "))
    idade = int(input("Qual a sua idade: "))
    sexo = str(input("Qual o seu sexo? F ou M: ")).upper()
    somaidade += idade
#Procurando o Homem mais velho.
    if p == 1 and sexo in 'M':
        maioridadeh = idade
        nomehvelho = nome
    if sexo in 'M' and maioridadeh < idade:
        maioridadeh = idade
        nomehvelho = nome
#Calcalando quantas mulheres tem menos de 20 anos.
    if sexo == 'F' and idade < 20:
        totalmulher20 += 1
#Calculando a média de idade do grupo.
mediaidade = somaidade / p
print('A média de idade do grupo é: {} anos'.format(mediaidade))
print('{} é o homem mais velho do grupo com {} anos'.format(nomehvelho, maioridadeh))
print('{} mulheres tem menos de 20 anos.'.format(totalmulher20))
