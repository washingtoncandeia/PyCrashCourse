import matplotlib.pyplot as plt

# Utilizando a função scatter()
plt.scatter(2,4, s=200)

# Organizando a apresentação do gráfico
plt.title('Square Numbers', fontsize=24)
plt.xlabel('Value', fontsize=14)
plt.ylabel('Square of Numbers', fontsize=14)

# Organizando gráfico
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
