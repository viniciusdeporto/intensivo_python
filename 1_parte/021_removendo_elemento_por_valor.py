motorcycle = ['honda', 'yamaha', 'suzuki', 'ducati']
# motorcycle.remove('yamaha')
too_expensive = "ducati"
motorcycle.remove(too_expensive)
print(motorcycle)
print(f'\nA {too_expensive.title()} is too expensive for me, I take the {motorcycle[2]}')