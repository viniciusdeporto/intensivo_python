def make_pizza(tamanho, *toppings):
    print('Faça uma lista com o seguinte ingrediente: ')
    for topping in toppings:
        print(f"\tFaça uma pizza de {tamanho} fatias de {topping}")
        
    # print(toppings)
    
make_pizza(16, 'pepperoni')
make_pizza(12, 'portuguesa', 'mussarela', '4 queijos')

