#Faça uma função "calcular_media" onde ela deve receber 3 notas e retornar a média entre as notas.

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

n1 =  float(input('Digite o primeiro numero: '))
n2 =  float(input('Digite o segundo numero: '))
n3 =  float(input('Digite o terceiro numero: '))

    
resultado = calcular_media(n1,n2,n3)

print(f'resultado das media = {resultado}')

