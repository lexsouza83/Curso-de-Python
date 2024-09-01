"""
Listas em python

Para criar uma Listas -> lanche = ['pão'. 'suco', 'pizzs','picole']
Uma lista pode ser alterada e a tupla não.
Podendo ter elementos adicinados, em qualquer posiçao da lista
Usando os metodos apppend e insert
Podemos tambpem excluir elementos da lista, através dos indices, usando o comando del, ex: del lanche[3]
e o método .pop, ex: lanche.pop[3]
Também, é possicel remover algum elemento usando o método remove, ex: lanche.remove('pizza'), indicando o elemento
que sera excluido ao invés do indice do mesmo.

"""
import random


def jogo_par_ou_impar():
    print("Bem-vindo ao Jogo de Par ou Ímpar!")
    jogador_nome = input("Digite seu nome: ")

    while True:
        try:
            jogador_escolha = int(input("Escolha um número (0 a 10): "))
            if jogador_escolha < 0 or jogador_escolha > 10:
                raise ValueError
            break
        except ValueError:
            print("Por favor, insira um número válido entre 0 e 10.")

    computador_escolha = random.randint(0, 10)

    total = jogador_escolha + computador_escolha
    resultado = "par" if total % 2 == 0 else "ímpar"

    print(f"{jogador_nome}, você escolheu {jogador_escolha}.")
    print(f"O computador escolheu {computador_escolha}.")
    print(f"Total: {total} ({resultado})")

    jogada_jogador = input("Você escolhe Par ou Ímpar (P/I)? ").lower()

    if (jogada_jogador == "p" and resultado == "par") or (jogada_jogador == "i" and resultado == "ímpar"):
        print(f"Parabéns, {jogador_nome}! Você ganhou!")
    else:
        print(f"Desculpe, {jogador_nome}. O computador ganhou.")

    jogar_novamente = input("Quer jogar novamente? (s/n): ").lower()
    if jogar_novamente != "s":
        print("Obrigado por jogar!")
        break

jogo_par_ou_impar()
