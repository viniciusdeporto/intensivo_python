users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'aeinstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie', 
        'last': 'curie',
        'location': 'paris'
    },
}

for username, user_info in users.items():
    print(f'\nUsername: {username}')
    full_name = f'{user_info['first']} {user_info['last']}'
    location = user_info['location']

    print(f'\tFull name: {full_name.title()}')
    print(f'\tlocation: {location.title()}')





#     coisas = {
#     'usuario_1':{
#         'nome': 'vinicius',
#         'sobrenome': 'Porto',
#         'cidade': 'araçatuba'
#     },

#     'usuario_2':{
#         'nome': 'maiara',
#         'sobrenome': 'cidinha',
#         'cidade': 'sao francisco'
#     }
# }

# print(coisas['usuario_1']['nome'])
# print(coisas['usuario_2'].keys()[0])