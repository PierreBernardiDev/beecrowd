numeroDeCedulas = int(input('isira a quantidade de cédulas: '))

notaCem = 0
notaCinquenta = 0
notaVinte = 0
notaDez = 0
notaCinco = 0
notaDois = 0
notaUm = 0
i = 0

print(numeroDeCedulas)

while numeroDeCedulas > i:
    if( numeroDeCedulas >= 100):
        notaCem += 1
        numeroDeCedulas -= 100
    elif (numeroDeCedulas >= 50):
        notaCinquenta += 1
        numeroDeCedulas -= 50
    elif (numeroDeCedulas >= 20):
        notaVinte += 1
        numeroDeCedulas -= 20
    elif(numeroDeCedulas >= 10):
        notaDez += 1
        numeroDeCedulas -= 10
    elif(numeroDeCedulas >= 5):
        notaCinco += 1
        numeroDeCedulas -= 5
    elif(numeroDeCedulas >= 2):
        notaDois += 1
        numeroDeCedulas -= 2
    else:
        notaUm += 1
        numeroDeCedulas -= 1

print(notaCem,'nota(s) de R$ 100,00')
print(notaCinquenta,'nota(s) de R$ 50,00')
print(notaVinte,'nota(s) de R$ 20,00')
print(notaDez,'nota(s) de R$ 10,00')
print(notaCinco,'nota(s) de R$ 5,00')
print(notaDois,'nota(s) de R$ 2,00')
print(notaUm,'nota(s) de R$ 1,00')