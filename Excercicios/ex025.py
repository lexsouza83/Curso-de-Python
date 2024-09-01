'''
Crie um programa que leia o nome de uma pessoa e diga se ele tem Silva no nome.
'''

print('='*20, 'NOMES', '='*20)
pessoa = str(input('Informe o seu nome completo:')).strip().title()
print('O Nome digitado contem o nome Silva?{}'.format('Silva' in pessoa))
