'''
Escreva um programa que leia um valor em metros e o exiba convertido em cm e mm.
'''
medida = float(input('Informe um distancia em metros: '))
cm = medida * 100
mm = medida * 1000
print('A medida de {}m corresponde a {}cm e a {}mm'.format(medida, cm, mm))
