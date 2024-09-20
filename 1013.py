valoresInput = str(input('insira os valores: '))

listaValores = [int(valor) for valor in valoresInput.split(' ')]

soma = (listaValores[0] + listaValores[1] + abs(listaValores[0] - listaValores[1])) / 2
""" maior = max(listaValores) """
maior = (soma + listaValores[2] + abs(soma - listaValores[2])) / 2

print(int(maior), ' eh o maior')