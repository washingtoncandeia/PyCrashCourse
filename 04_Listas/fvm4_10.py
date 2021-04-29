##---------------------
# Faça você mesmo cap.4
# p. 107 - 108
##---------------------

# 4.11 - Minhas pizzas, suas pizzas
pizzas = ['calabresa', 'marguerita', 'quatro queijos']
friend_pizzas = pizzas[:]
pizzas.append('pepperoni')
print(pizzas)

friend_pizzas.append('mussarela')
print(friend_pizzas)

# Exibindo frases
print('Minhas pizzas preferidas são: ')
for pizza in pizzas:
    print('- ' + pizza)


print('As pizzas favoritas do meu amigo são: ')
for pizza in friend_pizzas:
    print('- ' + pizza)
