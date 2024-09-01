"""
Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor foi digitado impar desconsidere-o.
"""
print("{:_^30}".format("Soma dos Pares"))
soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input("Digite um {}° número: ".format(c)))
    if n1 % 2 == 0:
        soma = soma + n1  #poderia ser assim: soma += n1
        cont = cont + 1  #poderia ser assim: cont += 1
print("A soma dos {} números pares é {}".format(cont, soma))