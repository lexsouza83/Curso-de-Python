"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
"""
from time import sleep
print("{:_^40}".format(" PALÍNDROMOS "))
frase = str(input("Digiete uma frase: ")).strip().lower().replace(" ","")
frasei = frase
print("""A frase informada é:{} 
E o seu inverso é: {}""".format(frase, frasei))
print("ANALISANDO A FRASE...")
sleep(2)
if frase == frasei[::-1]:
    print("Esta a frase é um PALÍNDROMO.")
else:
    print("Não é um PALÍNDROMO.")


