import random


Vendas = []


#('kevin, rua , 27 , tel , 45.5') 
#('kevin, rua , 27 , tel , 45.5') 
#('kevin, rua , 27 , tel , 45.5') 

while True:
    resp = input(' Deseja registrar uma nova venda? [S/N]-> ')
    if resp.upper() == 'N':
        break   


    cliente = input('Digite o nome do cliente ')
    endereço = input('Digite o endereço do cliente ')
    telefone = input('Digite o telefone do cliente ')
    valor = float(input('Digite o valor da compra '))

    venda = ( cliente , endereço , telefone , valor)
    Vendas.append(venda)


for venda in Vendas:
    print(f'- {venda[0]} , {venda[2]} , R${venda[3]:.2f}')

    sorteado = random.choice(venda)
    print('Sorteado' .center(30, '-'))
    print(f'Nome: {sorteado[0]}')
    print(f'Telefone: {sorteado[2]} ')
    print(f'endereço: {sorteado[1]}')
    print(f'Valor da compra: R${sorteado[3]:.2f}')

print('Fim Do Programa')