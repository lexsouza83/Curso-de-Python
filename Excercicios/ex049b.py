"""
Refaça o desafio 09, mostrando a tabuada de um número que o usuário escolher.
So que agora utilizando um laço for.
"""

print("{:_^50}".format('TABUADA 2.0'))
n1 = int(input("Digite o número para ver a tabuada: "))
op = int(input("""Qual operação deseja realizar? 
        [1] + Adição
        [2] * Muiltiplicação
        Sua Opção: """))
print("-="*30)
for tab in range(1,11):
    if op == 1:
        print("{:2} {} {:2} = {:2}".format(n1, ' +', tab, n1 + tab))
    elif op == 2:
        print("{:2} {} {:2} = {:2}".format(tab, ' x', n1, n1 * tab))

print("-="*30)
