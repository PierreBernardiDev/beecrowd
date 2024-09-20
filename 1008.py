numero = int(input())
horasTrabalhada = int(input())
valorHora = float(input())

salario = (horasTrabalhada * valorHora)

print("NUMBER =",numero)
print("SALARY = U$",'{:.2f}'.format(salario))