def soma_impares_entre(x, y):
    # Garantir que x seja menor que y
    if x > y:
        x, y = y, x
    
    soma = 0
    for i in range(x + 1, y):
        if i % 2 != 0:
            soma += i
    return soma

# Leitura dos valores de entrada
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

# Cálculo e exibição do resultado
resultado = soma_impares_entre(x, y)
print(resultado)