itensInput = str(input('insira os dados: '))

arrayItens = [
                [1,'Cachorro Quente',4.00],
                [2,'X-Salada',4.50],
                [3,'X-Bacon',5.00],
                [4,'Torrada simples',2.00],
                [5,'Refrigerante',1.50]
            ]

pedido = [int(itens) for itens in itensInput.split(' ')]

numeroPedido = pedido[0]
quantPedido = pedido[1]
soma = 0

for item in arrayItens:
    if item[0] == numeroPedido:
        soma = item[2] * quantPedido
        print('Total: R$ ''{:.2f}'.format(soma))
        break