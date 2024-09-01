'''
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar no serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que já passou do prazo.
'''

print('===== ALISTAMENTO MILITAR =====')

from datetime import date

nome = str(input('Informe o seu Nome Completo: '))
print('Informe a data completa do seu nascimento, ')
dianasc = int(input('Dia: '))
mesnasc = int(input('Mês: '))
anonasc = int(input('Ano: '))

#calculo da diferença de idade com base no ano de nascimento.
idadeatual = date.today().year - anonasc
#print(anoatual)
if idadeatual < 18:
    print('{} vocẽ tem atualmente {} anos'
          '\n O período de Alistamento Militar vem ai!'.format(nome, idadeatual))
elif idadeatual == 18:
    print('AS FORÇAS ARMADAS ESPERAM POR VOCÊ!'
          '\n {} com {} anos você deve se apresentar a Junta Militar mais proxima!'.format(nome, idadeatual))
else:
    print('{} com {} anos você perdeu o período de alistamento que foi há {} anos.'.format(nome, idadeatual, idadeatual - 18))
