a, b = map(int, input('Insira os valores: ').split())

soma = (a + b) % 2

if a % b == 0 or b % a == 0:
    print('Sao Multiplos')
else:
    print('Nao sao Multiplos')