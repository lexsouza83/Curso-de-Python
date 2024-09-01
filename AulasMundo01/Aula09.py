#Manupulando textos

#Fatiamento
frase = 'Curso em video Python'
print(frase[9]) # vai imprimir apenas a letra na posição 9
print(frase[9:14]) # vai imprimir a cadeia que vai da posição 9 atá a posição 13. A posição 14 fica de fora.
print(frase[9:21])
print(frase[9:21:2])#imprime a cadeia de caracteres pulando de 2 em 2.
print(frase[:5])

#Análie
'''
len - comprimento  - len(frase)
count - contagem = frase.count('o')'
find - busca uma letra ou expressão - frase.find('video')
in - contem um termo ou letra - 'Curso' in frase

'''

#Trasnformação
'''
replace - Substituir - frase.replace('Python', 'Android')
upper - Coloca a frase toda em Maúsculas - frase.upper()
lower - Cocloca a frase toda em minúsculas = frase.lower()
capitalize - Torna o primeiro caractere da frase para Maiúscula - frase.capitalize()
title - Colçoa as primeira letra de cada Palavra em Maiúsculas - frase.title()
'''

#Transformação
'''
strip - remove espaços no final e no inicio da string - frase.strip() - rstrip e lstrip

'''

#Divisão
'''
split - Faz a divisão da string de acordo com os espaçõs - frase.split()

'''
#Junção
'''
join - faz a junção de string divida usando o - hifen - '-'.join(frase) 
'''

#pratica

