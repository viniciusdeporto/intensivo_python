rios = {
    'rio nilo':'egito',
    'rio amazonas': 'brasil',
    'rio danubio': 'alemanha'
}

for nome, pais in rios.items():
    print(f'{nome.title()} atravessa o {pais.title()}')
    
print('------------------------------------')
    
for nome in rios.keys():
    print(f'Você conhece o {nome.title()}?')
    
print('------------------------------------')
    
for pais in rios.values():
    print(f'Dentro do {pais.title()} existe um rio.')