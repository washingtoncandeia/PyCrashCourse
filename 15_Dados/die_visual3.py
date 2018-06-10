import pygal
from die import Die

# die_visual.py - v3, p.441 com pygal
die = Die()

results = []
for roll in range(100):
    result = die.roll()
    results.append(result)

# Análise de resultados depende das frequencias
frequencias = []
for value in range(1, die.num_sides+1):
    # Da lista results, conta valores 1,2,3,4,5, e 6
    frequency = results.count(value)
    frequencias.append(frequency)

# Visualização de resultados
hist = pygal.Bar()

hist.title = "Results of rolling one D6 100 times"
hist.x_labels = ['1', '2', '3', '4', '5', '6']
hist.x_title = 'Result'
hist.y_title = 'Frequency of Result'

hist.add('D6', frequencias)
hist.render_to_file('die_visual.svg')
