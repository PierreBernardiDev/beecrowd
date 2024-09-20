numeros = input("Insira os números separados por espaço: ").split()
numeros = list(map(float, numeros))

# Usando list comprehension para contar os valores positivos
positivos = sum(1 for numero in numeros if numero >= 0)

print(f"{positivos} valores positivos")