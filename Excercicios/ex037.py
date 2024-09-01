'''
Ecreva um programa que leia um número inteiro qualquer e peça para o usuário escolher
qual será a base de conversão:
1 binário;
2 octal;
3 hexadecimal.
'''
print('----- BASES NÚMERICAS -----')
from  time import sleep
n1 = int(input('Digite um valor inteiro: '))
# bloco das conversões
binario = bin(n1)
octal = oct(n1)
hexa = hex(n1)

#menu
opcao = int(input('Escolha para qual base numérica deseja converter o valor digitado.'
      '\n 1 - Binário'
      '\n 2 - Octal'
      '\n 3 - Hexadecimal'
      '\nSua Escolha: '))

print('PROCESSANDO....')
sleep(3)

if opcao == 1:
    print('{} em Binário é igual a {}'.format(n1, binario[2:]))
elif opcao == 2:
    print('{} em Octal é igual a {}'. format(n1, octal[2:]))
elif opcao == 3:
    print('{} em Hexadecimal é igual a {}'.format(n1, hexa[2:]))
else:
    print('Opção incorreta! Tente novamente!')


