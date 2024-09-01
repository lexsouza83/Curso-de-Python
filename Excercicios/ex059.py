"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar [2] Multiplicar [3]Maior [4] Novos números [5] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.
"""
from time import  sleep
print('{:_^40}'.format('MENU DE OPERAÇÕES'))
opcao = ''
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
while opcao != '5':
    opcao = str(input("""Escolha a operação: 
[1] Adição | [2] Muiltiplicação | [3] Maior | [4] Digitar Novos Números | [5] Sair """))
    if opcao == '1':
        calc = n1 + n2
        print('Operação escolhida: Adição. Resultado: {}'.format(calc))
    elif opcao == '2':
        calc = n1 * n2
        print('Operação escolhida: Muiltiplicação. Resultado: {}'.format(calc))
    elif opcao == '3':
        if n1 > n2:
            calc = n1
        else:
            calc = n2
        print('Operação escolhida: Maior. O Maior número digitado foi: {}'.format(calc))
    elif opcao == '4':
        print('Informe novos números')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif opcao > '5' or opcao == '' or opcao == '0':
        print('Opção Invalida! Tente outra vez')
    sleep(2)
print('Finalizando...')
sleep(1)
print('Programa Encerrado!')
