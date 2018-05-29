import matplotlib.pyplot as plt

# Faça voce mesmo, p.427 - 15.2
numeros = list(range(1, 5001))
cubos = [x**3 for x in numeros]

# scatter
plt.scatter(numeros, cubos, c=cubos, cmap=plt.cm.OrRd, edgecolors='none', s=40)

# Organizando plot
plt.title('Quadrados', fontsize=26)
plt.xlabel('Números', fontsize=14)
plt.ylabel('Cubo de Números', fontsize=14)

# Eixos
plt.axis([0, 5100, 0, 50100000])

# Organizando figura
plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('cubos2.png', bbox_inches='tight')
# bbox_inches --> remove espaços em branco extras, do gráfico.