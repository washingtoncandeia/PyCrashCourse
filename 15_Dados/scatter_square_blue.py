import matplotlib.pypolot as plt

# scatter_squares.py, p.423
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

# Montando o gráfico
plt.scatter(x_values, y_values, s=100)

# Organizando o plot
plt.title('Square Numbers', fontsize=30)
plt.xlabel('Values', fontsize=16)
plt.ylabel('Square of Values', fontsize=16)

# Organizando a figura do gráfico
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

