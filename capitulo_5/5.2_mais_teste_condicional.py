# idade = 18
# vinicius = 33
# theo = 0
# if vinicius >= idade and theo <= idade:
#     print("os dois estão corretos")
# else:
#     print('Algo não esta correto')

# ingredientes = ['mostarda', 'farinha', 'ovo', 'sal', 'manteiga']

# if 'barbecue' not in ingredientes:
#     print('não temos, show')
# else:
#     print('temos')

# minha_idade = 33
# irmao_idade = 29

# if minha_idade == 20 and irmao_idade >= 22:
#     print('Na primeira condicao')
#     print('Uma pelo menos está certa\n') #so passa se os dois estiverem corretos
# else:
#     print('Na primeira condicao')
#     print('Os dois precisam estar corretos, se não a condição não funciona\n')



# if minha_idade == 20 or irmao_idade == 29:
#     print('na segunda condição')
#     print('pelo menos uma foi\n') #aqui so passa se um dos dois foram corretos.
# else:
#     print('na segunda condição')
#     print('nenhum foi queridao\n')

# nome = 'vinicius'
# if nome != 'vinicius':
#     print('Nome é diferente hein')
# else:
#     print('nome é igual')


# teste com operadores de igualdade e de diferença com strings:
# nome = 'vinicius'
# if nome == 'vinicius':
#     print(f'nome é {nome}')

# if nome != 'pedro':
#     print(f'O nome não é {nome}')

# teste usando o metodo lower():
# nomes = ['joao', 'guilherme', 'gustavo', 'felipe', 'diogo', 'Vinicius']
# for nome in nomes:
#     if nome.lower() == 'vinicius':
#         print(f'Achamos o nome {nome}')

#teste numerico com operadores de igualdade e de diferença, maior e menor que, maior ou igual que e menor ou igual a:
numero1 = 10
numero2 = 20

teste = 10
 
if numero1 == teste:
    print(f'O numero 1 é igual a {numero1}')

if numero2 != teste:
    print(f'O numero 2 é diferente de {teste}')

#Maior ou menor que:
    
if numero1 <= numero2:
    print(f"{numero1} é menor que {numero2}")
else:
    print(f'{numero1} é maior que {numero2}')

if numero2 >= numero1:
    print(f'{numero2} é maior que {numero1}')
else:
    print(f'{numero2} é menor que {numero1}')