'''
        CORREÇÃO DO GUSTAVO GUANABARA
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
- Se ele ainda vai se alistar no serviço militar
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que já passou do prazo.
'''

print('===== ALISTAMENTO MILITAR =====')

from datetime import  date

anoatual = date.today().year #variavel para pegar o ano atual.
nome = str(input('Infore o seu nome: '))
anonasc = int(input('Informe o seu ano de Nascimento: '))
idade = anoatual - anonasc #Calculando a idade atual do candidato.
print('{} você nasceu em {}, tem {} anos em {}.'.format(nome, anonasc,  idade, anoatual))
if idade == 18:
    print('Você deve se apresentar para o alistamento Militar! AS FORÇAS ARMADAS ESPERAM POR VOCÊ!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento'. format(saldo))
else:
    saldo = idade - 18
    print('Você já deveria ter se apresentado ao alistamento há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}.'.format(anoatual - saldo))


