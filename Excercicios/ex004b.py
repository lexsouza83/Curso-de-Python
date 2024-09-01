'''
Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo
e todas as informações possiveis.
'''
algo = input('Digite alguma coisa: ')
print('O tipo primitivo desse valor é: {} '.format(type(algo)))
print('É uma palavra? {}'.format( algo.isalpha()))
print('É um número: {}'.format(algo.isnumeric()))
print('É uma caractere alfanúmerico: {}'.format(algo.isalnum()))
print('Esta em letras minusculas: {}'.format(algo.islower()))
print('Esta em letras Maiusculas: {} '.format(algo.isupper()))
print('Esta capitalizado: {}'.format(algo.istitle()))