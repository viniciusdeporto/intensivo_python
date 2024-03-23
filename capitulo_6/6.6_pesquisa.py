favorite_linguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
}

lista = ['vinicius', 'djaw', 'jen', 'phil']
for nome in lista:
    if nome not in favorite_linguages.keys():
        print(f'{nome.title()} faça nossa pesquisa')
    else:
        print(f'{nome}, Obrigado por fazer nossa pesquisa')
    

