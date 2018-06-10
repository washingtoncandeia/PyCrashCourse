from die import Die

# die_visual.py, v2 - p.440
# Cria um dado de seis lados

die = Die()

# Armazenar resultados em uma lista
results = []

for roll_num in range(100):
    result = die.roll()
    results.append(result)

# Analisa os resultados
frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)
