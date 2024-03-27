cidades = {
    'araçatuba': {'pais': 'Brasil', 'população': 200000, 'fato': 'terra do boi gordo'},
    'nova york': {'pais': 'Estados Unidos', 'população': 8336817, 'fato': 'cidade que nunca dorme'},
    'londres': {'pais': 'Reino Unido', 'população': 8982000, 'fato': 'história com mais de 2.000 anos'}
}

for cidade, info in cidades.items():
    print(f"Você conhece {cidade.title()}?!")
    print(f"\tPaís: {info['pais']}")
    print(f"\tPopulação: {info['população']}")
    print(f"\tFato: {info['fato']}")
