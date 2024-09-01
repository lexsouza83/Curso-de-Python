"""
Faça um program que leia nome é média de um aluno, guardando também a situação em um dicionário.
No final mostre o conteúdo da estrutura na tela.
"""

print('-=' * 15)
print('MÉDIAS ESCOLARES')
print('-=' * 15)
dados = {}
boletim = []
while True:
    dados['Aluno:'] = str(input('Nome: ')).capitalize().strip()
    dados['Média:'] = float(input(f'Média de {dados["Aluno:"]}: '))
    boletim.append(dados.copy())
    op = str(input('Informar outro? S/N: ')).lower().strip()
    if 'n' in op:
        break
#analisando os dados informados
for b in boletim:
    print(b)
    print()
print(boletim)
