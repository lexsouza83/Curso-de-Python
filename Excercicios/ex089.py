"""
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre uma boletim contendo a média de cada um e permita que o usuário possoa mostra as notas de cada
aluno individualmente.

"""
print('-'*10, 'BOLETIM ESCOLAR','-'* 10)
from time import sleep
boletim = []
resp = ''
while True:
    aluno = str(input('Nome: ')).capitalize().strip()
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    resp  = str(input('Deseja continuar? S/N: ')).lower().strip()
    boletim.append([aluno, nota1, nota2])
    if 'n' in resp:
        break
print('-' * 7, 'CALCULANDO MÉDIA', '-' * 7)
sleep(1)

for p in boletim:
    print(f'O(A) Aluno(a) {p[0]} obteve média: {(p[1] + p[2]) / 2}')
print('-' * 20)

while True:
    op = str(input('Exibir boletim completo por aluno? S/N: ')).lower().strip()
    if 'n' in op:
        break
    else:
        nome = str(input('Digite o nome do aluno para ver seu boletim: ')).capitalize().strip()
        for p in boletim:
            if nome == p[0]:
                print(p)
                print('-' * 20)
print('FIM')
