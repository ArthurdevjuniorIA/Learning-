# 1. Leitura da primeira linha (N = total de alunos, K = mínimo de aprovados)
n, k = map(int, input().split())

# 2. Leitura da segunda linha (Lista com todas as notas)
notas = list(map(int, input().split()))

# 3. O Truque: Ordenar as notas do maior para o menor
notas.sort(reverse=True)

# 4. A Resposta: Pegar a nota que está na posição K (índice K - 1)
nota_de_corte = notas[k - 1]

# 5. Imprimir o resultado limpo
print(nota_de_corte)