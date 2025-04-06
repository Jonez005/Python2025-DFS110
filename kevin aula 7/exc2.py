#Ex02. Faça um programa que peça o nome e 3 notas de um aluno, essas informações devem ser salvas em um dicionário com as chaves "nome" e "notas" (notas deve ser uma lista com as 3 notas). 


#Aluno[]
#notas[]


aluno = {}

aluno['nome'] = input('Digite o nome do aluno: ')
aluno['notas'] = []

for i in range(3):
    nota = float(input(f'Digite a {i+1}ª nota: '))
    aluno['notas'].append(nota)

aluno['media'] = sum(aluno['notas']) / len(aluno['notas'])
aluno['situacao'] = 'APROVADO' if aluno['media'] >= 6 else 'REPROVADO'

print('----- Aluno ------')
for chave, valor in aluno.items():
    print(f'{chave.capitalize()}: {valor}')