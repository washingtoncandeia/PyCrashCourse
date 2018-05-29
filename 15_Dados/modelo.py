# Scatter
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Organizando plot
plt.title('Quadrados', fontsize=26)
plt.xlabel('Valores', fontsize=14)
plt.ylabel('Quadrado dos Valores', fontsize=14)

# Especificando limites do gráfico
plt.axis([0, 1100, 0, 1100000])

# Organizando figura
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('squares_plot.png', bbox_inches='tight')
# bbox_inches --> remove espaços em branco extras, do gráfico.