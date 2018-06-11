import matplotlib.pyplot as plt

x_axis = list(range(1,21))
y_axis = [
    3.5, 3.6, 3.6, 4.10, 4.5,
    4.8, 5.0, 4.3, 5.0, 4.0,
    4.5, 4.3, 4.6, 4.5, 5.3,
    3.5, 4.3, 4.2, 4.4, 4.2
]

plt.plot(x_axis, y_axis, '--', color='blue', marker='|', linewidth=1, markersize=5)
plt.scatter(x_axis, y_axis, c='blue', marker='8', edgecolors='none', s=50)

# Organizando plot
plt.title('Dureza - Extrato Hidroalcoólico', fontsize=22)
plt.xlabel('Unidades', fontsize=14)
plt.ylabel('Dureza (Kgf)', fontsize=14)

# Especificando limites do gráfico
plt.axis([0, 21, 2.5, 6])

# Organizando figura
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()