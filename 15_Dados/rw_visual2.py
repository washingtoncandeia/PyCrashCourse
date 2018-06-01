import matplotlib.pyplot as plt
from random_walk import RandomWalk

"""rw_visual.py, p.431"""
# Continua criando novos passeios aleatórios enquanto ativo
while True:
    rw = RandomWalk()
    rw.fill_walk()
    
    # Scatter plot
    plt.scatter(rw.x_values, rw.y_values, s=15)

    plt.show()

    # Garantindo que podemos parar a qualquer momento
    keep_running = input('Make another walk? (y/n): ')
    if keep_running == 'n':
        break

