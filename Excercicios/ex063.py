"""
Escreva u programa que leia um número n inteiro qualquer e mostre na tela os N primeiros elementos de uma
Sequência de Fibonacci.
Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
"""
print('{:_^30}'.format('SEQUENCIA FIBONACCI'))
num = int(input("Quantos termos deseja mostrar? "))
t1, t2 = 0, 1
c = 0
print('~'* 30)
while c < num:
    print('{}-> '.format(t1), end='')
    t1, t2 = t2, t1 + t2
    c += 1
print('FIM')
