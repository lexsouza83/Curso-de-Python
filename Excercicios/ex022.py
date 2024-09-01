'''
Crie uma programa que leia o nome completo de uma pessoa e mostre:
1 o nome com todas as letras Maiúsculas.
2 O nome com todas as letras minúsculas.
3 Quantas letra ao todo sem considerar os espaços.
4 Quantas letras tem o primeiro nome.
'''

print('='*20, 'ANALIANDO O TEXTO', '='*20)
nome = str(input('Informe o seu nome completo: '))
print('Este é o seu nome em letras Maiúsculas - ', nome.upper())
print('Este é o seu nome em letras minúsculas - ', nome.lower())
nome1 = nome.replace(" ","") #usei o comando replace para remover todos os  espaços da frase.
print('O seu nome completo tem {} letras.'.format(len(nome1)))
nome2 = nome.split()
print('O seu primeiro nome tem apenas',len(nome2[0]),' letras.')
print('='*10, 'FIM DA ANALISE', '='*10)




