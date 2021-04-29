#!/bin/env python
# p.158-9

aliens = []

# Cria 30 alienigenas verdes
for alien in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

# Mostra os 5 primeiros aliens
for alien in aliens[0:5]:
    print(alien)
print('...')