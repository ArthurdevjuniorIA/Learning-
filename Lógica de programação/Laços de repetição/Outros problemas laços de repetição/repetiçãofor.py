valores_impares = 0
for i in range(6):
    valor_aleatorio = int(input())
    if valor_aleatorio % 2 != 0:
        valores_impares+=1
print(f"{valores_impares} valor(es) ímpar(es)")