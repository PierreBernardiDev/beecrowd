tempoViagem = int(input('Tempo de viagem: '))
velocidadeMedia = int(input('velocidade média de viagem: '))

consumoAutomovel = 12

previsaoDeGastos = (velocidadeMedia * tempoViagem) / consumoAutomovel

print('{:.3f}'.format(previsaoDeGastos))