"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input("Qual o seu sexo? [M/F]:  ")).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    sexo = str(input("ERRO! Qual o seu sexo? [M/F]:  ")).strip().upper()[0]
print('Resposta {} gravada!'.format(sexo))

#Poderia ter sido montado assim -> while sexo not in 'MmFf'.