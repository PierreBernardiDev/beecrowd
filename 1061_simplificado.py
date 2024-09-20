from datetime import datetime

# Leitura da entrada
inicioDia = int(input().split()[1])
horaInicio = input().strip()
finalDia = int(input().split()[1])
horaFim = input().strip()

# Converte as entradas para objetos datetime
inicio = datetime.strptime(f"{inicioDia} {horaInicio}", "%d %H : %M : %S")
fim = datetime.strptime(f"{finalDia} {horaFim}", "%d %H : %M : %S")

# Calcula a diferença entre as datas
duracao = fim - inicio

# Extrai dias, horas, minutos e segundos da duração
dias = duracao.days
horas, resto = divmod(duracao.seconds, 3600)
minutos, segundos = divmod(resto, 60)

# Exibe o resultado
print(f"{dias} dia(s)")
print(f"{horas} hora(s)")
print(f"{minutos} minuto(s)")
print(f"{segundos} segundo(s)")
