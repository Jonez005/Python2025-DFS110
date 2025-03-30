#Faça um programa que peça 6 numeros e armazene-os em uma lista. Ao final, mostre a soma entre os numeros.

numeros = []

for n in range(6):
    numero =float(input(f'digite o {n} numero'))
    numeros.append(numero)

soma= sum(numeros)
print(soma)
