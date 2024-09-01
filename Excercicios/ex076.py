"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequencia.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""
print('.'* 50)
print('{:^50}'.format('Lista de Produtos').upper())
print('.' * 50)
produtos = ('Mouse', 21.50, 'Teclado', 49.90, 'Cabo USB', 9.99, 'PenDrive 16GB', 14.50, 'Cartão SD 32GB', 37.50
            ,'WebCam', 49.90, 'Adaptador USB/AUDIO', 32.50, 'Adaptador USB/WIFI', 59.90)
print(f'{produtos[0]:.<40}' + ' R$' + f' {produtos[1]:.2f}')
print(f'{produtos[2]:.<40}' + ' R$' + f' {produtos[3]:.2f}')
print(f'{produtos[4]}' + '.'* 40 + ' R$' + f' {produtos[5]}')
print(f'{produtos[6]}' + '.'* 40 + ' R$' + f' {produtos[7]}')
print(f'{produtos[8]}' + '.'* 40 + ' R$' + f' {produtos[9]}')
print(f'{produtos[10]}' + '.'* 40 + ' R$' + f' {produtos[11]}')
print(f'{produtos[12]}' + '.'* 40 + ' R$' + f' {produtos[13]}')
print(f'{produtos[14]}' + '.'* 40 + ' R$' + f' {produtos[15]}')
print('.' * 50)
