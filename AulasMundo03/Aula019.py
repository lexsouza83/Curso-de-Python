"""
Dicionarios - {}
pode ser declardo de 2 formas:
dados = dict()
dados = {}

dados = {'nome': 'Pedro', 'idade': 24}


filmes= {
    'Titulo': 'StarWars', 'ano': 1977, 'diretor': 'Geoger Lucas'
}
print(filmes.values()) #Imprime apenas os valores
print(filmes.keys()) #Imprime as chaves
print(filmes.items()) #Imprime tanto valores quanto chaves

for k,v in filmes.items():
    print(f'O {k} é {v}')
"""
#Prática:
pessoas = {'nome': 'Alex ', 'sexo': 'M', 'idade': 39}
print(pessoas)
print(pessoas['nome'])

