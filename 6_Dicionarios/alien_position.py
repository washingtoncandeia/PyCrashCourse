#!/bin/env python

# Cap.6, p.144

alien_0  = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}

# Mover alienigena de acordo com a velocidade.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# A nova posicao é a posicao antiga somada ao incremento.
alien_0['x_position'] += x_increment

print('Nova posiçao: ' + str(alien_0['x_position']))
