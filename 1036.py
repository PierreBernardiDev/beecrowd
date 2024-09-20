import math

values = str(input('Insira os valores: '))

splitValues = [float(valor) for valor  in values.split(' ')]

a = splitValues[0]
b = splitValues[1]
c = splitValues[2]

if(a == 0):
    print('Impossivel calcular')
else:
    delta =  b * b - 4 * a * c
    if(delta < 0):
        print('Impossivel calcular')
    else:
        r1 = (-b + math.sqrt(delta)) /  (2*a)
        r2 = (-b - math.sqrt(delta)) /  (2*a)
        print('R1 = ''{:.5f}'.format(r1))
        print('R2 = ''{:.5f}'.format(r2))