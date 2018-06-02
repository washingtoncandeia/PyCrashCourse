import matplotlib.pyplot as plt
from random_walk3 import RandomWalk

# rw_visual.py, p.434 (Limpando eixos)
while True:
     # Cria um passeio aleatório e plota os dados
    rw = RandomWalk()
    rw.fill_walk()

    point_numbers = list(range(rw.num_points))

    plt.scatter(
        rw.x_values, rw.y_values,
        c=point_numbers, cmap=plt.cm.Blues,
        edgecolors='none', s=15
    )
    
    # Enfatiza o primeiro número
    plt.scatter(
        0, 0, c='green',
        edgecolors='none', s=100
    )
    
    # Enfatiza o último número
    plt.scatter(
        rw.x_values[-1], rw.y_values[-1],
        c='red', edgecolors='none', 
        s=100
    )

    # Remove os eixos
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # keep running
    keep_running = input('Make anohter walk? (y/n): ')
    if keep_running == 'n':
        break

