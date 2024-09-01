'''
DEsenvolva uma lógica que leia o peseo e a altura da pessoa. calcule o seu IMC e mostre seu status.
de acordo com a tabela abaixo.
- Abaixo de 18.5kg : Abaixo do Peso
- Entre 18.5kg e 25kg : Peso Ideal
- De 25kg a 30kg : Sobrepeso
- De 30kg a 40kg : Obesidade
- Acima de 40 : Obesidade Mórbida
'''
print('_____ CALCULANDO IMC _____')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura ** 2)
if imc <= 18.5:
    print('{:.2f} - ABAIXO DO PESO'.format(imc))
elif imc > 18.5 and imc < 25:
    print('{:.2f} - PESO IDEAL'.format(imc))
elif imc > 25 and imc < 30:
    print('{:.2f} - SOBREPESO'.format(imc))
elif imc > 30 and imc < 40:
    print('{:.2f} - OBESIDADE'.format(imc))
else:
    print('{:.2f} - OBESIDADE MORBIDA'.format(imc))


