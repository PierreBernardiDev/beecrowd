import math

primeira_entrada = input('Insira a posição de x1 e y1: ')
segunda_entrada = input('Insira a posição de x2 e y2: ')

x1_y1 = [float(valor_x) for valor_x in primeira_entrada.split(' ')]
x2_y2 = [float(valor_y) for valor_y in segunda_entrada.split(' ')]

distancia = math.sqrt((x1_y1[0] - x2_y2[0])**2 + (x1_y1[1] - x2_y2[1])**2)

print('{:.4f}'.format(distancia))