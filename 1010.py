array = [
         [12, 1, 5.30],
         [16, 2, 5.10],
        ]

valor_total = 0

for linha in array:
    quantidade = linha[1]
    preco = linha[2]
    valor_total += quantidade * preco

# Exibindo o valor total a pagar
print(f'VALOR A PAGAR: R$ {valor_total:.2f}')