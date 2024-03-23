favorite_linguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

friends = ['phil', 'sarah']
for name in favorite_linguages.keys():
    print(f'Hi {name.title()}')
    if name in friends:
        language = favorite_linguages[name].title()
        print(f'\t{name.title()}, I see you love {language}')

if 'erin' not in favorite_linguages.keys():
    print('Erin, take our poll!')
if 'vinicius' not in favorite_linguages.keys():
    print('Meu querido vinicius, faça nossa enquete ai')