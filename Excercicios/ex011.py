'''
Faça uma programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
necessária para pinta-la. Sabendo cada litro de tina pinta uma área de 2m².
'''
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = larg * alt
print('Sua parede tem a seguinte area {}m²'
      '\nPara pintar essa parede, será necessário {}l de tinta'.format(area, (area/2)))

