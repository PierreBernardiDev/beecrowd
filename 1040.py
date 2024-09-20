inputNotas = str(input('Insira as notas: '))

p1 = 2
p2 = 3
p3 = 4
p4 = 1

notas = [float(nota) for nota in inputNotas.split(' ')]

mediaAluno = round(((notas[0] * p1) + (notas[1] * p2) + (notas[2] * p3) + (notas[3] * p4)) / 10, 1)
mediaFinal = 0

print('Media: {:.1f}'.format(mediaAluno))

if mediaAluno >= 5 and mediaAluno < 7:
    print('Aluno em exame')
    inputRecuperacao = float(input('Insira a nota da recuperação: '))
    mediaFinal = (mediaAluno + inputRecuperacao) / 2
    print('Nota do exame: {:.1f}'.format(inputRecuperacao))
    if mediaFinal >= 5:
        print('Aluno aprovado')
    else:
        print('Aluno reprovado')
    print('Media final: {:.1f}'.format(mediaFinal))
elif mediaAluno >= 7:
    print('Aluno aprovado')
else:
    print('Aluno reprovado')
