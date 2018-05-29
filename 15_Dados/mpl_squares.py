import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares, linewidth = 5)                # Parametro linewidth controla espessura da linha

# Títulos e eixos
plt.title('Apenas um Teste', fontsize = 32)     # Funcao title define o título do gráfico

# xlabel e ylabel sao funçoes 
# para definir titulos aos eixos
plt.xlabel('Nada', fontsize = 16)               # Parametro fontsize controla o tamanho do texto no gráfico
plt.ylabel('Números', fontsize = 16)            # Parametro fontsize controla o tamanho do texto no gráfico

# Define o tamanho do rótulo das marcaçoes
plt.tick_params(axis='both', labelsize = 14)    # Funcao tick_params estiliza as marcaçoes nos eixos
