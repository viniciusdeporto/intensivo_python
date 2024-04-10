dicionario = {}

active = True
while active:
    nome = input('Qual o seu nome? ')
    sobrenome = input('Qual seu sobrenome? ')

    dicionario[nome] = sobrenome

    repeat = input('colocar mais nomes e sobrenomes? (s/n)')
    if repeat == 'n':
        active = False

print('--- Resultado ---')
for nome, sobrenome in dicionario.items():
    print(f'{nome} {sobrenome}')

# print(dicionario)