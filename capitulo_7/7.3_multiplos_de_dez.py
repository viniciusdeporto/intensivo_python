numero = input('Vamos ver se o numero de sua escolha é multiplo de 10, digite um numero: ')
numero = int(numero)

if numero % 10 == 0:
    print('O numero é multiplo de 10, show de bola!')
else:
    print('Infelizmente o numero não da pra ser dividido.')