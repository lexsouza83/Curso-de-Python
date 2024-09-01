'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possiveis.
'''
algo = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é: ', type(algo))
print('É uma palavra?', algo.isalpha())
print('É um número: ', algo.isnumeric())
print('É uma caractere alfanúmerico', algo.isalnum())
print('Esta em letras minusculas: ', algo.islower())
print('Esta em letras Maiusculas, ', algo.isupper())