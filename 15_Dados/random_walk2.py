from random import choice

class RandomWalk():
    """
    Versão 2 do módulo random_walk, com modificações. 
    Exercício 15.4, Faça Vocẽ Mesmo, p.437
    """
    def __init__(self, num_points=5_000):
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points

        # Todos os passeios começam na coordenada (0,0)
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        """Calcula todos os pontos do passeio, aleatoriamente."""

        # O passeio precisa chegar a um ponto ou tamanho desejado
        # Continuar dando os passos até o passeio alacançar este tamanho:
        while len(self.x_values) < self.num_points:

            # Direção a ser seguida: direita [1], esquerda [-1]
            x_direction = choice([1])  # Retirado -1

            # Distância a ser seguida
            x_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

            # Determinar o tamanho do passo
            x_step = x_direction * x_distance


            # Repetir para eixo y:
            # Direção a ser seguida: diretia [1], esquerda [-1]
            y_direction = choice([1])   # Retirado -1

            # Distância a ser seguida
            y_distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

            # Determinar o tamanho do passo
            y_step = y_direction * y_distance

            # Movimentos que não irão a lugar algum têm valor 0
            # Para rejeitá-los usar logica:
            if x_step == 0 and y_step == 0:
                continue

            # Calcula os próximos valores de x e y
            next_x = self.x_values[-1] + x_step    # Utiliza o último valor da lista ([-1])
            next_y = self.y_values[-1] + y_step    # Utiliza o último valor da lista ([-1])

            self.x_values.append(next_x)
            self.y_values.append(next_y)

