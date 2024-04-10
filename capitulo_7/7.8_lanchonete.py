pedidos = ['x-salada', 'x-bacon', 'x-egg', 'x-tudo']
pedidos_finalizados = []

active = True
while pedidos:
    pedidos_atuais = pedidos.pop()

    print(f'Seu pedido, {pedidos_atuais} está pronto')
    pedidos_finalizados.append(pedidos_atuais)

index = 1
for pedidos_prontos in pedidos_finalizados:
    print(f'Pedido {index}: {pedidos_prontos}')
    index += 1


