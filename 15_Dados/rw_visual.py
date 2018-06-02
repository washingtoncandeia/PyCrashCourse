import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Cria um passeio aleatório e plota os pontos
rw = RandomWalk()   # Intancia, cria passeio aletório e o armazena em rw
rw.fill_walk()

# Plotar o gráfico
plt.scatter(rw.x_values, rw.y_values, s=15)

plt.show()
