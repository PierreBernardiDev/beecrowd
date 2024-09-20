inicio, fim = map(int, input('Insira os dados: ').split())

def calcular_duracao(hora_inicio, hora_fim):
    if hora_inicio < hora_fim:
        duracao = hora_fim - hora_inicio
    else:
        duracao = (24 - hora_inicio) + hora_fim
    return duracao

duracao = calcular_duracao(inicio, fim)

print(f"O JOGO DUROU {duracao} HORA(S)")