# idade = int(input('\nDigite sua idade: '))


# if idade <= 3:
#     print('Entrada Gratuita')
# elif idade > 3 and idade <= 12:
#     print('Entrada custa R$ 12,00 Reais')
# elif idade > 12:
#     print('Entrada custa R$ 15,00 Reais')



active = True
while active:
    idade = input('\nDigite sua idade ou "q" para sair: ')

    if idade.lower() == 'q':
        break

    idade = int(idade)

    if idade <= 3:
        print('Entrada Gratuita')
    elif idade > 3 and idade <= 12:
        print('Entrada custa R$ 12,00 Reais')
    elif idade > 12:
        print('Entrada custa R$ 15,00 Reais')
