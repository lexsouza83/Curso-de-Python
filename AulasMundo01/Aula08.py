'''
Aula 08 - Utilizando módulos.
Usamos o comando import para importar todos os recursos do módulo.
Usamos os comandos from nome do módulo import para importar um recurso especifico.
'''

import math #importamos a biblioteca inteira.
n1 = int(input('informe um número: '))
raiz = math.sqrt(n1)
print('a raiz de {} é igual a {}'.format(n1, math.ceil(raiz)))

# Outra forma de importar recursos de uma módulo

from math import sqrt, ceil #importamos apenas 2 recursos da biblioteca.
n1 = int(input('informe um número: '))
raiz = sqrt(n1)
print('a raiz de {} é igual a {}'.format(n1, ceil(raiz)))