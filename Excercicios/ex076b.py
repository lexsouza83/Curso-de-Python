"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
print('.'* 50)
print('{:^50}'.format('Lista de Produtos').upper())
print('.' * 50)
produtos = ('Mouse', 21.50, 'Teclado', 49.90, 'Cabo USB', 9.99, 'PenDrive 16GB', 14.50, 'Cartão SD 32GB', 37.50
            ,'WebCam', 49.90, 'Adaptador USB/AUDIO', 32.50, 'Adaptador USB/WIFI', 59.90)
for intem in range(0, len(produtos)):
    if intem % 2==0:
        print(f'{produtos[intem]:.<40}', end='')
    else:
        print(f'R${produtos[intem]:6.2f}')
print('.' * 50)
