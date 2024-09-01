'''
Crie um algoritmo que leia um número e moste o seu dobro, o triplo e sua raiz quadrada.
'''
print('='*15,'Calculos','='*15)
n1 = int(input('Informe um número: '))
print('O número digitado foi: {} '
      '\nO seu dobro é igual a {}'
      '\nO seu triplo é igual a {}'
      '\nSua raiz quadrada é igual a {:.2f}'.format(n1, n1*2, n1*3, n1**(1/2)))
