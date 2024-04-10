prompt = 'Se pudesse ir para qualquer lugar do mundo para onde iria? '
prompt += 'deseja sair? (s/n)'


lugares = []
while True:
    mensagem = input(prompt)

    if mensagem == 's':
        break
    else:
        lugares.append(mensagem)

print('Lugares que gostaria de visitar')
for lugar in lugares:
    print(lugar)

