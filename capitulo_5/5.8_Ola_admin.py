usuarios = ['vinicius', 'levi', 'admin', 'joao', 'pedro']
for usuario in usuarios:
    if usuario == 'admin':
        print(f'Olá {usuario}, gostaria de ver o relatorio de status?')
    else:
        print(f'Olá, {usuario}, Obrigado por fazer login novamente!')