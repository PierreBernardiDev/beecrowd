numeros = []

entrada = input(f"Insira os números separados por espaço: ")
valores = list(map(float, entrada.split()))
numeros.extend(valores)

negativos = 0

for i, numeros in enumerate(numeros):
    if numeros >= 0:
        negativos += 1

print(negativos,'valores positivos')
