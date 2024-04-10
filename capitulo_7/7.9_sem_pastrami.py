sandwich_orders = ['pastrami', 'x-salada', 'pastrami', 'x-bacon', 'x-egg', 'pastrami', 'x-tudo']
print(sandwich_orders)
print('Infelizmente estamos sem sanduiches de pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

print(sandwich_orders)
