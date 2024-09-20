inicioHora, inicioMin, fimHora, fimMin = map(int, input('Insira os dados: ').split())

def calcular_duracao(hora_inicio, min_inicio, hora_fim, min_fim):
    if hora_inicio == hora_fim and min_inicio == min_fim:
        duracaoH = 24
        duracaoMin = 0
    else:
        if hora_inicio < hora_fim or (hora_inicio == hora_fim and min_inicio < min_fim):
            duracaoH = hora_fim - hora_inicio
            duracaoMin = min_fim - min_inicio
        else:
            duracaoH = (24 - hora_inicio) + hora_fim
            duracaoMin = min_fim - min_inicio
        
        if duracaoMin < 0:
            duracaoMin += 60
            duracaoH -= 1

    return duracaoH, duracaoMin

duracaoH, duracaoMin = calcular_duracao(inicioHora, inicioMin, fimHora, fimMin)

print(f"O JOGO DUROU {duracaoH} HORA(S) E {duracaoMin} MINUTO(S)")


