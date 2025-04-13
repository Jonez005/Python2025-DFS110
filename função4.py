# retunr saida

#  O  retunr, premite que a gente envie um valor para o local onde a funçao foi chamada.


def saudação(nome = '' ):
    if nome == '':
        return 'olá'  
    else:
        return f'olá, {nome}'

nome= input(' Digite seu nome (<ENTER> caso não queira informar): ')
mensagem = saudação(nome)
print(mensagem)