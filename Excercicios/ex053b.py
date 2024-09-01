"""
Crie um programa que leia uma frase qualquer e diga se ela é um palindromo, desconsiderando os espaços.
                CORREÇÃO DO GUSTAVO GUANABARA
"""

print("{:_^40}".format(" PALÍNDROMOS "))
frase = str(input("Digite uma frase: ")).strip().upper()
separa = frase.split()
junto = "".join(separa)
inverso = ""
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(junto, inverso))
if inverso == junto:
    print("Temos um Palíndromo!")
else:
    print("A frase digitada não é um Palíndromo!")

"""
        CODIGO DOS COMENTÁRIOS DO YOUTUBE
frase = input("Qual a frase? ").upper().replace(" ", "")
if frase == frase[::-1]:
    print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
"""