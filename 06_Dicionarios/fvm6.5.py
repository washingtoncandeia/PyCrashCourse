#!/bin/env python
# Faça voce mesmo, p.155

rios = {
    'amazonas': 'brasil',
    'yangtze': 'china',
    'missisipi': 'E U A',
}

for rio, pais in rios.items():
    print('\nO rio ' + rio.title() + ' pertence a(o/s): ' + pais.title() + '.')