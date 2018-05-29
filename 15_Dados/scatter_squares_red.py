import matplotlib.pyplot as plt

# scatter_squares.py, p.426
# Parametro c='color'

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# Scatter
plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)

# Organizando o plot
plt.title('Quadrados', fontsize=26)
plt.xlabel('Valores', fontsize=14)
plt.ylabel('Quadrados dos Valores', fontsize=14)

plt.axis([0, 1100, 0, 1100000])

# Organizando a figura
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
