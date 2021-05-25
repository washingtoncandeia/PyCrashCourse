## Cap.4 - pt.2

# Looping
players = ['charles', 'martina', 'michael', 'florence', 'eli']

for player in players[1:4]:
    print(player.title())
    
# Copiando listas
my_foods = ['pizza', 'arroz e feijão', 'ravioli', 'lasanha']
my_friends_food = my_foods[:]

print('Minha lista de comidas favoritas: ' + str(my_foods) + '.')
print('A lista dos meus amigos: ' + str(my_friends_food) + '.')

# modificando
my_foods.append('pudim')
my_friends_food.append('sorvete')


print('Minha lista de comidas favoritas: ' + str(my_foods) + '\n.')
print('A lista dos meus amigos: ' + str(my_friends_food) + '.')
