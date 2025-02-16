nota1 = float(input('digite a primeira nota'))
nota2 = float(input('digite a segunda nota'))
nota3 = float(input('digite a terceira nota'))

media = (nota1 + nota2 + nota3) / 3

if media >= 6:
    situação = 'aprovado'
elif media <4:
    situação = 'reprovado'
else: 
    situação = 'recuperação'

# Saída
print(f'Média: {media:.2f}')
#rint(f'Situação: {situacao}')
