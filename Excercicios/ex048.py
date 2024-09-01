"""
Faça um programa que calcule a soma entre todos os números impares que são multiplos de 3 e que se encontrem
no intervalo de 1 até 500.
"""
print('{:_^30}'.format('MULTIPLOS DE 3'))
soma = 0
cont = 0
for n1 in range(1, 501, 2):
    if n1 % 3 == 0:
        soma = soma + n1 #Acumulador
        cont = cont + 1  # contador
print("A soma de todos os {} valores pedidos é {}".format(cont, soma))
