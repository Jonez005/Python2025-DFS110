idade = int(input('digite sua idade'))

if idade < 16:
    print('nao pode votar')
elif (idade >= 16 and idade < 18) or idade >= 65:
    print('voto faucltativo')
else:
    print('voto obrigatorio')    