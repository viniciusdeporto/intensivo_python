favorite_linguages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python'
}

print('The fallowing languages have been mentioned:')
for languages in set(favorite_linguages.values()):
    print(languages.title())

