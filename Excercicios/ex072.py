"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de 0 até 20.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
print('.'* 50)
print('{:^50}'.format('TRANSFORMANDO NÚMEROS'))
print('.'* 50)

numExtenso = ('Zero','Um', 'Dois', 'Três', 'Quantro','Cinco', 'Seis','Sete','Oito','Nove','Dez'
              ,'Onze','Doze','Treze','Quatorze', 'Quinze', 'Dezesseis', 'Dezesete','Dezoito', 'Dezenove', 'Vinte')
num = int(input('Digite qualquer número de 0 a 20: '))
while num < 0 or num > 20:
        num= int(input('Tente outra vez. Digite qualquer número de 0 e 20: '))
print(f'O número digitado foi {numExtenso[num]}')
