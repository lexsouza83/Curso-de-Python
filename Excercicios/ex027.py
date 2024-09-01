'''
Faça uma programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e último nome separadamente.
'''
print('='*20, 'NOMES', '='*20)
pessoa = str(input('Informe o seu nome completo:')).strip().title()
pessoa = pessoa.split()
print('Este é o seu primeiro nome: {}'.format(pessoa[0]))
print('Este é o seu último nome: {}'.format(pessoa[len(pessoa) - 1]))
