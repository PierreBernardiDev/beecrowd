renda = float(input('Insira a renda: '))

if renda == 0 or renda <= 2000.00:
    print('Isento')
elif 2000.01 <= renda <= 3000.00:
    imposto = (renda - 2000.00) * 0.08
    print(f"Imposto a pagar: R$ {imposto:.2f}")
elif 3000.01 <= renda <= 4500.00:
    imposto = (renda - 3000.00) * 0.18 + 80.00
    print(f"Imposto a pagar: R$ {imposto:.2f}")
elif renda > 4500.00:
    imposto = (renda - 4500.00) * 0.28 + 350.00
    print(f"Imposto a pagar: R$ {imposto:.2f}")
