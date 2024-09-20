# Número de casos de teste
N = float(input())

# Para cada caso de teste
for _ in range(N):
    # Lê os três valores reais
    valores = list(map(float, input().split()))
    
    # Calcula a média ponderada
    media_ponderada = (valores[0] * 2 + valores[1] * 3 + valores[2] * 5) / 10
    
    # Imprime a média ponderada com uma casa decimal
    print(f"{media_ponderada:.1f}")
