def definePar(numero):
    resultado = ""
    if numero % 2 == 0:
        resultado = "Par"
    else:
        resultado = "Impar"

    return resultado

print(definePar(5))