valores = str(input())

lista_floats = [float(valor) for valor in valores.split()]
pi = 3.14159

triangulo = lista_floats[0] * lista_floats[2] / 2
circulo = lista_floats[2] * lista_floats[2] * pi
trapezio = (lista_floats[0] + lista_floats[1]) * lista_floats[2] / 2
quadrado = lista_floats[1] * lista_floats[1]
retangulo = lista_floats[0] * lista_floats[1]

print('TRIANGULO: ''{:.3f}'.format(triangulo))
print('CIRCULO: ''{:.3f}'.format(circulo))
print('TRAPEZIO: ''{:.3f}'.format(trapezio))
print('QUADRADO: ''{:.3f}'.format(quadrado))
print('RETANGULO: ''{:.3f}'.format(retangulo))
