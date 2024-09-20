numeros = str(input('insira os valores: '))

separarNumeros = [int(valor) for valor in numeros.split(' ')]

somaAb = 0
somaCd = 0
a = 0

somaAb += separarNumeros[0] + separarNumeros[1]
somaCd += separarNumeros[2] + separarNumeros[3]

a += separarNumeros[0] % 2

if(separarNumeros[1] > separarNumeros[2] and separarNumeros[3] > separarNumeros[1] and somaCd > somaAb and somaAb >= 0 and somaCd >= 0 and a == 0):
    print('Valores aceitos')
else:
    print('Valores nao aceitos')