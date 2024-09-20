numero1 = float(input('insira o valor: '))
numero2 = float(input('insira o valor: '))
numero3 = float(input('insira o valor: '))
numero4 = float(input('insira o valor: '))
numero5 = float(input('insira o valor: '))

valoresPares = 0

if numero1 % 2 == 0:
    valoresPares += 1
if numero2 % 2 == 0:
    valoresPares += 1
if numero3 % 2 == 0:
    valoresPares += 1
if numero4 % 2 == 0:
    valoresPares += 1
if numero5 % 2 == 0:
    valoresPares += 1

print(valoresPares,'valores pares')