X = int(input("Digite um valor inteiro positivo: "))


if X % 2 == 0:
    X += 1

for i in range(6):
    print(X + 2 * i)