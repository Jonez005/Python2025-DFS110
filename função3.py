
#podemos tornar um parametro opcional, definindo um valor padrão para quando ele nao for informado

def saudação(nome = '' ):
    if nome == '':    
        print(f'olá,')  
    else:
        print(f'olá, {nome}')

saudação()
saudação('julesca')