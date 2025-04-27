
# 1 - Faça um algoritmo utilizando função que receba um número e defina se ele é positivo negativo ou nulo(0)

def definir(num):
    i=''
    if num > 0:
        i = 'Positivo'
    elif num == 0:
        i = 'Nulo'
    else:
        i = 'Negativo'
    return i    
        

print(definir(5))

        