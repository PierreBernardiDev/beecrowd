numero1 = int(input('Insira o primeiro valor: '))
numero2 = int(input('Insira o segundo valor: '))
numero3 = int(input('Insira o terceiro valor: '))
numero4 = int(input('Insira o quarto valor: '))
numero5 = int(input('Insira o quinto valor: '))

numeroPar = 0
numeroImpar = 0
numeroPositivo = 0
numeroNegativo = 0

valores = [numero1, numero2, numero3, numero4, numero5]

for numero in valores:
    if numero % 2 == 0:
        numeroPar += 1
    else:
        numeroImpar += 1
    
    if numero > 0:
        numeroPositivo += 1
    elif numero < 0:
        numeroNegativo += 1

# Exibe os resultados
print(numeroPar, 'valor(es) par(es)')
print(numeroImpar, 'valor(es) impar(es)')
print(numeroPositivo, 'valor(es) positivo(s)')
print(numeroNegativo, 'valor(es) negativo(s)')