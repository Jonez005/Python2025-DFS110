#Fa;a um programa que peca 3 notas. ao final mostre as notas e a media entre elas.

notas = []

# Preenchimento da Lista
for n in range(3):
    nota = float(input(f'Digite a {n+1} nota '))
    notas.append(nota)

    # Mostrar os Elementos da Lista
    # 1

#qtd_notas = len(notas)

#print('Notas:')
#for n in range(qtd_notas):
  #  print(f'-{notas[n]:.2f}')

  #2
for nota in notas:
    print(f'- {nota:.2f}')

media = sum(notas) / len(notas)
print(f'media: {media:.2f}')