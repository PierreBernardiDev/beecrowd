numeroDeCedulas = str(input('isira a quantidade de cédulas: '))

separarMoedas = [int(valor) for valor in numeroDeCedulas.split('.')]


# notas

notaCem = 0
notaCinquenta = 0
notaVinte = 0
notaDez = 0
notaCinco = 0
notaDois = 0
notaUm = 0

# moedas
moedas = 0
moedaUm = 0
moedaCinquenta = 0
moedaVintCinco = 0
moedaDez = 0
moedaCinco = 0
moedaUmCent = 0

# variaveis while
notas =+ separarMoedas[0]
moedas =+ separarMoedas[1]

while notas > 0:
    if( notas >= 100):
        notaCem += 1
        notas -= 100
    elif (notas >= 50):
        notaCinquenta += 1
        notas -= 50
    elif (notas >= 20):
        notaVinte += 1
        notas -= 20
    elif(notas >= 10):
        notaDez += 1
        notas -= 10
    elif(notas >= 5):
        notaCinco += 1
        notas -= 5
    elif(notas >= 2):
        notaDois += 1
        notas -= 2
    else:
        moedaUm =+ 1
        notas -= 1

while moedas > 0:
    if moedas >= 100:
        moedaUm += 1
        moedas -= 100
    elif moedas >= 50:
        moedaCinquenta += 1
        moedas -= 50
    elif moedas >= 25:
        moedaVintCinco += 1
        moedas -= 25
    elif moedas >= 10:
        moedaDez += 1
        moedas -= 10
    elif moedas >= 5:
        moedaCinco += 1
        moedas -= 5
    else:
        moedaUmCent += 1
        moedas -= 1

print("NOTAS:")
print(notaCem,'nota(s) de R$ 100.00')
print(notaCinquenta,'nota(s) de R$ 50.00')
print(notaVinte,'nota(s) de R$ 20.00')
print(notaDez,'nota(s) de R$ 10.00')
print(notaCinco,'nota(s) de R$ 5.00')
print(notaDois,'nota(s) de R$ 2.00')

print("MOEDAS:")
print(moedaUm, 'moeda(s) de R$ 1.00')
print(moedaCinquenta, 'moeda(s) de R$ 0.50')
print(moedaVintCinco, 'moeda(s) de R$ 0.25')
print(moedaDez, 'moeda(s) de R$ 0.10')
print(moedaCinco, 'moeda(s) de R$ 0.05')
print(moedaUmCent, 'moeda(s) de R$ 0.01')