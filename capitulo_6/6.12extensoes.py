cidades = {
    'araçatuba': {
        'pais': 'brasil',
        'população': 200.000,
        'fato': 'terra do boi gordo'
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

for cidade, info in cidades.items():
    print(f'{cidade.title()}: {info['pais'].title()}')
    print(f'Populaçação: {info['população']}')
    print(f'Fato: {info['fato']}')