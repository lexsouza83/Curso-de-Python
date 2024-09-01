"""
Crie um programa que tenha uma tupla com várias palavras (Não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

"""
from re import findall
print('.'* 50)
print('{:^50}'.format('ANALISANDO PALAVRAS'))
print('.'* 50)
palavras = ('valor', 'recuperar', 'exemplo', 'quantidade','estoque'
            , 'contendo','produto', 'elementos', 'convertidos', 'desempacotar')
for p in range(0, len(palavras)):
    print(f'Na palavra {palavras[p].upper()},' , end='')
    vogais = ((findall("[aeiou]", palavras[p])))
    print(f' temos essas vogais: {vogais}')
