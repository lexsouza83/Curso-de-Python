'''
Crie qum programa que leia duas notas de um aluno e calcule sua média. mostrando um mensagem no final.
de acordo com a média atingida.
1 - Média abaixo de 5.0 REPROVADO
2 -  Média entre 5.0 e 6.9 RECUPERAÇÃO
3 - Média 7.0 ou superior APROVADO.
'''
print('===== BOLETIM ESCOLAR =====')
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input('Informe a segunda nota: '))
media = (nota1 + nota2) / 2
print('A Média obtida com as notas foi {}'.format(media))
if media >= 7:
    print('O aluno está APROVADO!')
elif media < 6.9 and media >=5:
    print('O aluno está em RECUPERAÇÃO!')
else:
    print('O aluno está REPROVADO!')
