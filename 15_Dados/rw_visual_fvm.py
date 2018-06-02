import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Faça você mesmo, p.437
# 15.3 - Movimento molecular

while True:
    rw = RandomWalk()
    rw.fill_walk()

    
    plt.plot(
        rw.x_values, rw.y_values, 
        color='blue', marker='.', 
        linewidth=1, markersize=5
        )

    # Organizando o plot
    plt.title(
        'Percurso de um Grão de Pólen na Água',
        fontsize=24
    )

    # Enfatiza o primeiro número
    plt.scatter(
        0, 0, 
        c='green', edgecolors='none', 
        s=300
    )
    
    # Enfatiza o último número
    plt.scatter(
        rw.x_values[-1], rw.y_values[-1],
        c='red', edgecolors='none', 
        s=300
    )

    plt.xlabel('Movimento Horizontal', fontsize=14)
    plt.ylabel('Movimento na Vertical', fontsize=14)
    
    plt.tick_params(axis='both', labelsize=14)
    
     # Remove os eixos
     ### axes() --> deprecated
     ### This is equivalent to 'pyplot.sca'
    #plt.axes().get_xaxis().set_visible(False)
    #plt.axes().get_yaxis().set_visible(False)

    plt.show()

    # keep running
    keep_running = input('Make anohter walk? (y/n): ')
    if keep_running == 'n':
        break
