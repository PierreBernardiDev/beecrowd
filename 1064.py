numero1 = float(input('insira o valor: '))
numero2 = float(input('insira o valor: '))
numero3 = float(input('insira o valor: '))
numero4 = float(input('insira o valor: '))
numero5 = float(input('insira o valor: '))
numero6 = float(input('insira o valor: '))

valoresPositivos = 0
valorMedia = 0

if numero1 >= 0:
    valoresPositivos += 1
    valorMedia += numero1
if numero2 >= 0:
    valoresPositivos += 1
    valorMedia += numero2
if numero3 >= 0:
    valoresPositivos += 1
    valorMedia += numero3
if numero4 >= 0:
    valoresPositivos += 1
    valorMedia += numero4
if numero5 >= 0:
    valoresPositivos += 1
    valorMedia += numero5
if numero6 >= 0:
    valoresPositivos += 1
    valorMedia += numero6

calculoMedia = valorMedia / valoresPositivos

print(valoresPositivos,'valores positivos')
print('{:.1f}'.format(calculoMedia))