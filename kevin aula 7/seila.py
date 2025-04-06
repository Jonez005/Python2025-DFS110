texto = input("Digite um texto: ")

# Cria um dicionário para armazenar as quantidades de cada letra
contador = {}

# Itera sobre cada caractere do texto
for letra in texto:
    if letra.isalpha():  # Verifica se o caractere é uma letra (ignora espaços e pontuações)
        letra = letra.lower()  # Converte a letra para minúscula para garantir que maiúsculas e minúsculas sejam contadas como iguais
        if letra in contador:
            contador[letra] += 1  # Incrementa o contador da letra
        else:
            contador[letra] = 1  # Adiciona a letra ao dicionário com contador 1

# Exibe o dicionário resultante
print("Quantidade de letras no texto:", contador)