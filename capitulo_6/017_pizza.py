pizza = {
    'crust': 'thick',
    'topping': ['mushroom', 'extra cheese']
}

print(f'You ordered a {pizza['crust']}-crust pizza')

for topping in pizza['topping']:
    print(f'\t{topping}')
