cidades = {
    'araçatuba': {
        'pais': 'brasil',
        'população': 200.000,
        'fatos': 'terra do boi gordo'
    },

    'nova york': {
        'pais': 'estados unidos',
        'população': '8.336.817',
        'fato': 'cidade que nunca dorme'
    },

    'londres': {
        'pais': 'reino unido',
        'população': '8.982.000',
        'fato': 'historia com mais de 2.000 anos'
    }
}

for cidade, coisas in cidades.items():
    print(f'voce conhece {cidade.title()}?!')
    for coisa, fatos in coisas.items():
        print(f'\t{coisa.title()}: {fatos}')