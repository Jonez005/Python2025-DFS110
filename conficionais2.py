nm1 = int(input('digite o primeiro numero'))
nm2 = int(input('digite o seugndo numero '))


#o elif ira ser avaliado caso o if seja 'falso'
#voce pode ter quantos 'elif' voce quiser entre o 'if'e o 'else'
if nm1 > nm2:
    print(f'o maior numero é {nm1}')
elif nm1 == nm2:
    print('os numeros sao iguais')
else:
    print(f'o maior numero é {nm2}')