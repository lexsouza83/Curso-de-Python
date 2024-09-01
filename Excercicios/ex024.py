'''
Crie um program a que leia o nome de uma cidade e diga se ela começa ou não com o nome Santo.
'''
print('='*20, 'CIDADES', '='*20)
city = str(input('Digite o nome da sua cidade: ')).strip().lower().split()
print('O nome informado começa com a palavra Santo? {}'.format('santo' in city[0]))
