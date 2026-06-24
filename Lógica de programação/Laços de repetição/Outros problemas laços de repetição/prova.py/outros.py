# Questão 1

3 # código da solução
numero = int(input())
print("<select>")
entre_tags = 1
for i in range(numero):
    print(f"<option>{entre_tags+i}</option>") 

# Questão 2

3 # código da solução
n = int(input())
z = "" 
for i in range(n):
    z = z + "z"
print(f"Ba{z}inga!")

# Questão 3

3 # código da solução
quantidade_alunos = 0
alunos = input()
primeiro_aluno = alunos
ultimo_aluno = " "
while True:
    alunos = input()
    if alunos != "fim":
        ultimo_aluno = alunos
        penultimo_aluno = ultimo_aluno
        quantidade_alunos+=1
    if alunos == "fim":
        break
print(f"Primeiro aluno: {primeiro_aluno}")
print(f"Último aluno: {ultimo_aluno}")
print(f"Total de alunos: {quantidade_alunos}")

# Questão 4

3 # código da solução
dias_analisados = int(input())
precipitacao_esperada = float(input())
diaria_valor = 0
for i in range(dias_analisados):
    valores_diarios = int(input())
    diaria_valor = valores_diarios+diaria_valor
print(f"Chuva acumulada: {diaria_valor:.1f} mm")
if diaria_valor>precipitacao_esperada:
    print("Acima do esperado")
elif diaria_valor == precipitacao_esperada:
    print("Dentro do esperado")
else:
    print("Abaixo do esperado")