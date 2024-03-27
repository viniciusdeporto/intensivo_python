favorite_places = {
    'vinicus': ['itapema', 'araçatuba', 'ceu'],
    'maiara': ['vinicius', 'ombro do vincius', 'abraço do vincius'],
    'cidinha': ['sao francisco', 'rio de janeiro', 'brasilia']
}

for nome, lugar in favorite_places.items():
    print(f'\nOs lugares favoritos do(a) {nome.title()}:')
    for lugares in lugar:
        print(f'{lugares.title()}')
 