from die import Die

# Cria um dado de seis lados
# D6
die = Die()

# Armazenar resultados em uma lista
results = []
for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)
