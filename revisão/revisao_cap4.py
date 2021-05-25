## Cap.4 - pt.1
# Exemplos
magicians = ['alice', 'david', 'carolina']

for magician in magicians:
    print(f'O nome do mágico é {magician.title()}!')
      
# 4-1 Pizzas
pizzas = ['pepperoni', 'calabresa', 'marguerita']

for piz in pizzas:
    print(f'A pizza de {piz} é uma das que mais gosto.')

print('Eu gosto muito de pizza!')

cubos = [cubo**3 for cubo in range(1, 11)]
print(cubos)

# exemplo
squares = []

for square in range(1, 11):
    square = square**2
    squares.append(square)

print(squares)

# exemplo 2
squares = []

for square in range(1, 11):
    squares.append(square**2)
    
print(squares)

# List comprehension
squares = [square**2 for square in range(1, 11)]
print(squares)
