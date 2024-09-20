salario = float(input('Insira os dados: '))

reajuste = 0
novoSalario = 0

if salario <= 400:
    reajuste = salario * 0.15
    salario += reajuste
    print('Novo salario: ''{:.2f}'.format(salario))
    print('Reajuste ganho: ''{:.2f}'.format(reajuste))
    print('Em percentual: 15 %')
elif salario > 400 and salario <= 800:
    reajuste = salario * 0.12
    salario += reajuste
    print('Novo salario: ''{:.2f}'.format(salario))
    print('Reajuste ganho: ''{:.2f}'.format(reajuste))
    print('Em percentual: 12 %')
elif salario > 800 and salario <= 1200:
    reajuste = salario * 0.10
    salario += reajuste
    print('Novo salario: ''{:.2f}'.format(salario))
    print('Reajuste ganho: ''{:.2f}'.format(reajuste))
    print('Em percentual: 10 %')
elif salario > 1200 and salario <= 2000:
    reajuste = salario * 0.07
    salario += reajuste
    print('Novo salario: ''{:.2f}'.format(salario))
    print('Reajuste ganho: ''{:.2f}'.format(reajuste))
    print('Em percentual: 7 %')
else:
    reajuste = salario * 0.04
    salario += reajuste
    print('Novo salario: ''{:.2f}'.format(salario))
    print('Reajuste ganho: ''{:.2f}'.format(reajuste))
    print('Em percentual: 4 %')