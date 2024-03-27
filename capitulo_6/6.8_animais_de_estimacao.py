pet_1 = {
    'animal': 'cachorro',
    'nome': 'bob',
    'dono': 'vinicius',
}

pet_2 = {
    'animal': 'cachorro',
    'nome': 'mel',
    'dono': 'maiara'
}

pet_3 = {
    'animal': 'gato',
    'nome': 'fred',
    'dono': 'nikolas'
}

pets = [pet_1, pet_2, pet_3]

for animais in pets:
    print('\ninformações sobre o Pet')
    for chave, valor in animais.items():
        print(f'{chave}: {valor}')
