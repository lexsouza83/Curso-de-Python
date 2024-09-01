"""
Faça um programa que leia o peso de 5 pessoas. No final, mostre qual foi o maior e o menor peso lidos.
"""
print('{:_^30}'.format('BALANÇA'))
maiorp = float(0)
menorp = float(0)
for p in range(1, 6):
    peso = float(input('Digite o peso da {}ª pessoa: Kg '.format(p)))
    if p == 1:
        maiorp = peso
        menorp = peso
    else:
        if peso > maiorp:
            maiorp = peso
        elif peso < menorp:
            menorp = peso
print('-='*30)
print('O maior peso lido foi:{}Kg e o menor foi: {}Kg'.format(maiorp, menorp))
print('-='*30)
