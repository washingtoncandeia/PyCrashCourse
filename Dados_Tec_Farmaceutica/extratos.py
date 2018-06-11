import pygal

dureza_ext_hidroal = [
    3.50, 3.60, 3.60, 4.10, 4.50, 4.80, 5.00, 4.30, 5.00, 4.00,
    4.50, 4.30, 4.60, 4.50, 5.30, 3.50, 4.30, 4.20, 4.40, 4.20
]


dureza_cel_agua = [
    15.39, 10.10, 12.79, 11.89, 9.39, 12.79, 6.89, 10.20, 10.29, 9.89, 
    13.20, 8.89, 11.09, 9.29, 7.79, 13.99, 7.60, 8.39, 10.20, 12.09
]

line_chart = pygal.Line()
line_chart.title = 'Dureza (Kgf)\nExtrato Hidroalcoólico\n Extrato Celulose/Água'
line_chart.x_labels = map(str, range(1, 21))
line_chart.y_labels = list(range(2, 17))
line_chart.add('Extrato Hidroalcoólico', [n for n in dureza_ext_hidroal])
line_chart.add('Extrato Celulose/Água',  [n for n in dureza_cel_agua])

line_chart.render_to_png('dureza.png')