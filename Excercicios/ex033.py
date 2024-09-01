'''
Faça um programa qie leia três números e mostre qual é o maior e qual é o menor entre eles.
'''
print('______ MAIOR E MENOR ______')
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Mais um número: '))
# encontrando o menor número:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# encontrando o maior  múmero:
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor número entre os 3 digitados é: {}' .format(menor))
print('O maior número entre os 3 digitados é: {}'.format(maior))
