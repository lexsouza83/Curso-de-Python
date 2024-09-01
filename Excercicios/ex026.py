'''
Faça um programa que leia frase pelo taclado e mostre:

1 Quantas vezes aparece a letra A
2 Em que posição ela aparece primeiro.
3 Em que posição ela aparece na última vez.
'''
print('='*20, 'ANALIANDO FRASES', '='*20)
frase = str(input('Digite uma frase qualquer: ')).strip().lower()
print('Na frase digitada a letra A aparece {}, vezes.'.format(frase.count('a')))
print('A letra A aparece primeiro na posição:{}'.format(frase.find('a')+1))
print('A última vez em que a letra A aparece é na possição: {}'.format(frase.rfind('a')+1))


