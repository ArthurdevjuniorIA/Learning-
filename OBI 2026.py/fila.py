quantidade_alunos = int(input())
alunos_nao_visiveis = 0
altura_aluno = list(map(int,input().split()))
maior_altura_encontrada = altura_aluno[-1]
for i in range(quantidade_alunos -2,-1,-1):
    if altura_aluno[i]>maior_altura_encontrada:
        maior_altura_encontrada = altura_aluno[i]
    else:
        alunos_nao_visiveis+=1
        
print(alunos_nao_visiveis)