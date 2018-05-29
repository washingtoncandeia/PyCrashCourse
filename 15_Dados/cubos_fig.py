import matplotlib.pyplot as plt

# Faça voce mesmo, p.427 - 15.1
numeros = [1, 2, 3, 4, 5]
cubos = [x**3 for x in numeros]

# scatter
plt.scatter(numeros, cubos, c=cubos, cmap=plt.cm.Oranges, edgecolors='none', s=40)

# Organizando o plot
plt.title('Cubos', fontsize=24)
plt.xlabel('Números', fontsize=14)
plt.ylabel('Cubo de Números', fontsize=14)

# Eixos
plt.axis([0, 6, 0, 140])

# Organizando a figura
plt.tick_params(axis='both', labelsize=14)

plt.savefig('cubos.png', bbox_inches='tight')
# bbox_inches --> remove espaços em branco extras, do gráfico.
