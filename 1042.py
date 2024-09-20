numeros = input('Insira os números: ')

arrayNumeros = [int(splitNum) for splitNum in numeros.split(' ')]

lista_crescente = sorted(arrayNumeros)
lista_decrescente = sorted(arrayNumeros, reverse=True)

for num in lista_crescente:
    print(num)

print('')

for num in arrayNumeros:
    print(num)