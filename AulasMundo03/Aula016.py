"""
Aula 16
Listas, Discionarios e Tuplas - Variáveis compostas
pode conter vários elementos, e esses elementos pode acessados por meio de indices.
#  >>>Tuplas não pode ser alteradas<<<
"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in lanche:
    print(f'Eu querer um(a) {comida}')
print('.'* 50)
for cont in range(0, len(lanche)):
    print(f'Eu vou querer um(a) {lanche[cont]} na posição {cont}')
print('.'* 50)
for pos, comida in enumerate(lanche):
    print(f'Eu vou querer um(a) {comida} na posição {pos}')
print('.'* 50)
print('Nossa comi feito um Animal!')