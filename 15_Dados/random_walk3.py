from random import choice

class RandomWalk():
    """Uma classe para gerar passeios aleatórios"""

    def __init__(self, num_points=5_000):
        """Inicializa os atributos de um passeio."""
        self.num_points = num_points

        # Todos os passeios começam na coordenada (0,0)
        self.x_values = [0]
        self.y_values = [0]

    
    def get_step(self):
        """Determina a direção e distancia de cada passo."""
        direction = choice([1, -1])
        distance = choice([0, 1, 2, 3, 4])
        step = direction * distance
        return step
        
    
    def fill_walk(self):
        """Calcula todos os pontos do passeio, aleatoriamente."""

        # O passeio precisa chegar a um ponto ou tamanho desejado
        # Continuar dando os passos até o passeio alacançar este tamanho:
        while len(self.x_values) < self.num_points:

            # Decisão da direação a ser tomada
            # Adicionar self. Do contrário, ficara indefinido
            x_step = self.get_step()
            y_step = self.get_step()
            
            # Rejeitar movimentação que não leva a lugar algum
            if x_step == 0 and y_step == 0:
                continue

            # Calcular os próximos valores de x e y
            next_x = self.x_values[-1] + x_step    # Utiliza o último valor da lista ([-1])
            next_y = self.y_values[-1] + y_step    # Utiliza o último valor da lista ([-1])

            self.x_values.append(next_x)
            self.y_values.append(next_y)
