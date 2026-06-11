nota_aluno = list(map(float,input().split()))
media = (nota_aluno[0]+nota_aluno[1])/2
if media>=7:
    print("Aprovado")
elif media>=4:
    print("Recuperacao")
else:
    print("Reprovado")