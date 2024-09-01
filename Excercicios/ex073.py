"""
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol.
Na orderm de colocação. Depois mostre:
a) Apenas os 5 primeiros colocados;
b) Os últimos colocados da tabela;
c) Uma lista com os times em ordem alfabética;
d) Em que posição da tabela está o time da Chapecoense.
"""
print('-'* 50)
print('{:^50}'.format('TABELA DO BRASILEIRÃO 2023'))
print('-'* 50)

classificacao = ('Botafogo','Palmeiras','Grêmio', 'Flamengo','Fluminense'
                 ,'Bragantino','Athletico-PR','Fortaleza','Atlético-MG','Cuiabá'
                 ,'São Paulo', 'Cruzeiro','Corinthias','Internacional','Goias'
                 ,'Bahia','Santos','Vasco', 'América-MG', 'Coritiba')
print(f'Classificação Geral do Brasileirão: {classificacao}')
print('-'* 50)
print(f'Cinco primeiros colocados: {classificacao[0:5]}')
print('-'* 50)
print(f'Quatro últimos colocados: {classificacao[16:20]}')
print('-'* 50)
listaOrdenanda = sorted(classificacao)
print(f'Classificaçaõ Alfabética: {listaOrdenanda}')
print('-'* 50)
print('A Equipe Chapecoense foi Eliminadada competição!')