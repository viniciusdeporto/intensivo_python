pessoa_1 = {
    'first_name': 'maiara',
    'last_name': 'souza',
    'age': 27,
    'city': 'São Francisco',
}

pessoa_2 = {
    'first_name': 'vinciius',
    'last_name': 'porto',
    'age': 34,
    'city': 'araçatuba',
}

pessoa_3 = {
    'first_name': 'matheus',
    'last_name': 'porto',
    'age': 32,
    'city': 'sao carlos',
}

pessoas = [pessoa_1, pessoa_2, pessoa_3]

for pessoa in pessoas:
    nome = pessoa['first_name'].title()
    sobrenome = pessoa['last_name'].title()
    idade = pessoa['age']
    cidade = pessoa['city'].title()
    print(f'Nome: {nome} {sobrenome}, Idade: {idade}, cidade {cidade}')
