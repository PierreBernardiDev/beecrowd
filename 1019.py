quantDias = int(input('digite a quantidade de dias: '))
ano = 0
mes = 0
dias = 0
i = 0

while (quantDias > i):
    if(quantDias >= 365):
        ano += 1
        quantDias -= 365
    elif(quantDias >= 30):
        mes += 1
        quantDias -= 30
    else:
        dias += 1
        quantDias -= 1

print(ano,'ano(s)')
print(mes,'mes(es)')
print(dias,'dia(s)')

