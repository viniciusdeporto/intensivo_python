favorite_linguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

print('The fallowing languages have been mentioned:')
for languages in favorite_linguages.values():
    print(languages.title())


# print('\nOutra forma de acessar os valores')
# for linguas in favorite_linguages:
#     print(f'as linguas sao {favorite_linguages[linguas]}')

# print(favorite_linguages)

# for name, languages in favorite_linguages.items():
#     print(name, languages)