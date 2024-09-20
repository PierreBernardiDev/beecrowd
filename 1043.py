a, b, c = map(float, input('Insira os valores: ').split())

if a + b > c and a + c > b and b + c > a:
    perimetro = a + b + c
    print('Perimetro =',perimetro)
else:
    area = ((a + b) * c) / 2
    print('Area =', area) 
