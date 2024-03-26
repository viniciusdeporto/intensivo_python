aliens = []

for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

    if alien['color'] == 'yellow' or alien['color'] == 'green' and alien['points'] == 10 and alien['speed'] == 'medium':
        alien['color'] = 'red'
        alien['points'] = 15
        alien['speed'] = 'fast'


for alien in aliens[:6]:
    print(alien)
print('...')