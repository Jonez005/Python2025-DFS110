ano = int(input('digite um ano:'))
if ano <= 100 and ano % 4 == 0:
    print(f'o ano digitado ({ano}) é um ano bissexto')
elif ((ano % 4) == 0 and (ano % 100)!=0)or ano % 400 ==0:
    print(f'o ano digitado ({ano}) é um ano bissexto')
else:
    print(f'o ano digitado ({ano}) nao e um ano bissexto')

    #Faça um programa que peça um ano, e informe se ele é um ano bissexto.
#BS: para ser bissexto, o ano deve ser divisivel por 4 e não pode ser divisivel por 100, exceto os divisiveis por 400.