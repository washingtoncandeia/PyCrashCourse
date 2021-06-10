# Listas em Dicionários
# 09 de junho de 2021

pizzas = {
    'borda': 'fina',
    'ingredientes': ['cogumelos', 'queijo extra']
}

print(f"Você pediu pizza com borda {pizzas['borda']}.")

for k, v in pizzas.items():
    print(f'{k.title()}: {v}.')

# Forma 1
for topp in v:
    print(topp)
