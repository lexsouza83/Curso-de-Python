"""
Crie um programa onde o usuário possa digitar 5 valores nunéricos e casdastre-os em uma lista, já na posição correta
de inserção (sem usar o sort()). No final mostre a lista ordenada na tela.
"""
print('-='*40)
print('ORDENANDO NÚMEROS')
print('-='* 40)
lista = []
for c in range(0, 5):
    n = int(input('Informe um valor: '))
    # Verifica se o valor digitado é maior que zero ou se é maior que o último elemento da lista.
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
    # determina em qual posição os proximos valores informados seram inseridos na lista.
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print('-='* 40)
print(f'Os valores informados em ordem são: {lista}')


