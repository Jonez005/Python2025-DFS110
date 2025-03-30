#Ex01. Faça um programa que peça as informações de uma pessoa (nome, altura e idade) e armazene em um dicionário, ao final mostre as informações dessa pessoa.


Pessoa = {}

Pessoa['nome'] = input('Digite seu nome ')
Pessoa['altura'] = input('Digite sua altura ')
Pessoa['idade'] = input('Digite sua idade ')

print('Pessoas: ')
print(f'nome: {Pessoa['nome']}')
print(f'altura: {Pessoa.get('altura')}')
print(f'idade:  {Pessoa.get('idade')}')