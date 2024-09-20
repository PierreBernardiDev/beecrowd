numeros = input()

lista_numeros = numeros.split()

numeros_inteiros = [int(elemento) for elemento in lista_numeros]

for i in range(len(numeros_inteiros)):
    if numeros_inteiros[i] == 0:
        print("NULL")
    else:
        if numeros_inteiros[i] % 2 == 0:
            if numeros_inteiros[i] > 0:
                print("EVEN POSITIVE")
            else:
                print("EVEN NEGATIVE")
        else:
            if numeros_inteiros[i] > 0:
                print("ODD POSITIVE")
            else:
                print("ODD NEGATIVE")
