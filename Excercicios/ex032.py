'''
Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
'''
print('______ ANO BISSEXTO ______')
from datetime import date # módulo importado para analise do ano atual.
ano = int(input('Informe o ano que deseja analisa ou digite 0 para o ano atual: '))
if ano == 0:
    ano = date.today().year # condição para analisar o ano atual do computador.
if ano % 100 != 0 and ano % 4 == 0 or ano % 400 == 0:
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))