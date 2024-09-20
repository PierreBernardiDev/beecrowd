N = int(input("Digite um valor inteiro N (N < 10000): "))

# Verifique todos os números de 1 a 10000
for i in range(1, 10001):
    if i % N == 2:
        print(i)