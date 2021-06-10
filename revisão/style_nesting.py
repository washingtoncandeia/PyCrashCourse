bandas = []

# looping para criar dicionarios
for n in range(1, 11):
    for bands in range(10):
        n = str(n)
    info = {f'estilo {n}'.title(): 'stoner'.title(), 'ano'.title(): 1993}
    bandas.append(info)

for band in bandas:
    print(band)
