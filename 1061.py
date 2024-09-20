def converte_horas(inicioDia, horaInicio, finalDia, horaFim):
    horaInicial, minutoInicial, segundosInicial = map(int, horaInicio.split(':'))
    horaFinal, minutoFinal, segundosFinal = map(int, horaFim.split(':'))

    horarioInicio = (horaInicial * 3600) + (minutoInicial * 60) + segundosInicial
    horarioFim = (horaFinal * 3600) + (minutoFinal * 60) + segundosFinal

    dias = int(finalDia) - int(inicioDia)


    if horarioFim < horarioInicio:
        dias -= 1
        horarioFim += 24 * 3600 

    duracaoTempo = horarioFim - horarioInicio

    horas = (duracaoTempo % (24 * 3600)) // 3600
    minutos = ((duracaoTempo % (24 * 3600)) % 3600) // 60
    segundos = ((duracaoTempo % (24 * 3600)) % 3600) % 60

    print(f"{dias} dia(s)")
    print(f"{horas} hora(s)")
    print(f"{minutos} minuto(s)")
    print(f"{segundos} segundo(s)")

inicioDia = input().split()[1]
horaInicio = input().strip()
finalDia = input().split()[1]
horaFim = input().strip()

converte_horas(inicioDia, horaInicio, finalDia, horaFim)

