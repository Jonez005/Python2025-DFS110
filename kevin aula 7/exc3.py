#Ex03. Faça um programa que peça um texto para o usuário e crie um dicionário que irá conter todas as letras e suas respectivas quantidades, exemplo:

letras = {}

texto = input('Digite seu texto ').upper()

for i in texto:
    if i == '-':
        continue

    i = i.lower()
    if letras.get(i) is None:
        letras[i] = 1

    else:
        letras[i] += 1

print(letras)