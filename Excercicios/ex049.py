"""
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher.
So que agora utilizando um laço for.
"""

print("{:_^50}".format('TABUADA 2.0'))
n1 = int(input("Digite o número para ver a tabuada: "))
for cont in range(1, 11):
    print('{:2} X {:2} = {:2}'.format(cont, n1,  n1 * cont))
